#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Following pygame example from: https://riptutorial.com/pygame/example/14697/a-simple--game-

"Boba Go Round" (working title)

Pretty much Sushi Go Round (Miniclip - https://www.miniclip.com/games/sushi-go-round/en/#privacy-settings)
but making boba drinks instead of sushi dishes

Coded and run using Python 3.9.7 and Spyder3

Created on Sun Jul  3 17:15:47 2022

@author: Garance Merholz
"""

# make a boba menu, e.g. with white jelly
# shouldn't click out before 2 seconds of seeing day won screen (tried with wait)
# it keeps going after allgoalswonImg lol
# thenumber goes to -1 after failure first day goals

# rect_example = pygame.Rect((0, 0), (32, 32))  # First tuple is position (from topleft corner), 
                                                # second is size.

import pygame
import sys
import random


###################################### SETUP
successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures".format(successes, failures))

# Window setup
original_width, original_height = 177, 140 # my boba backdrop's width, height (were 148, 140)
scaling_factor = 5
original_screen = pygame.Surface((original_width,original_height))
fullwindow = pygame.display.set_mode((scaling_factor*original_width, scaling_factor*original_height))  
pygame.display.set_caption('Boba Go Round')
clock = pygame.time.Clock()
FPS = 30  # This variable will define how many frames we update per second.
BLACK = (0, 0, 0)

def exitgame(): # define for when I need to exit
    print("Exited the game loop. Game will quit...")
    pygame.quit()
    sys.exit()

def show_numbers_in_font(fontstring,thenumber,toplefttuple,gapbwdigits):
    zeroImg = pygame.image.load("{0}_0.png".format(fontstring))
    zeroimgwidth = zeroImg.get_size()[0]
    to_add = zeroimgwidth+gapbwdigits
    midtuple = (toplefttuple[0]+to_add, toplefttuple[1])
    righttuple = (toplefttuple[0]+2*to_add, toplefttuple[1])
    original_screen.blit(pygame.image.load("{0}_{1}.png".format(fontstring,int(thenumber%10))),righttuple)
    if thenumber//100 != 0 or (thenumber//10)%10 != 0:
        original_screen.blit(pygame.image.load("{0}_{1}.png".format(fontstring,int((thenumber//10)%10))),midtuple)
    if thenumber//100 != 0:
        original_screen.blit(pygame.image.load("{0}_{1}.png".format(fontstring,int(thenumber//100))),toplefttuple)

def remove_cup_large():
    showcuplarge = False
    showcuplargeempty = False
    showtapioca = False
    showice = False
    highlightlid = False
    highlightstraw = False
    topchosen = False
    bottomchosen = False
    return showcuplarge, showcuplargeempty, showtapioca, showice, highlightlid, highlightstraw, topchosen, bottomchosen

def serve_customer(customer1location_scaled,fullcustomers_width_scaled,
                   showrequest,topchosen,highlightstraw,highlightlid,
                   showcupsmallgiven,custwaiting,cupsmallgiven_location,givennumbot,
                   givennumtop,givenstrawnum,giventapioca,timecustserved,surpriseme,
                   givenice,gavesurprise,cupsmallnumbot,cupsmallnumtop,smallstrawnum,
                   smalllidnum,smalltapioca,smallice,happyorangry,goalsmode,speedrun,
                   angrycustcount):
    xymouse_tuple = pygame.mouse.get_pos()
    customerclicked = int(6-((customer1location_scaled[0]+fullcustomers_width_scaled)-xymouse_tuple[0])/(fullcustomers_width_scaled/6))
    if showrequest[customerclicked] and all([topchosen, highlightstraw, highlightlid]): 
        # the large cup has to be full and lid-ed and straw-ed to serve
        showcupsmallgiven[customerclicked] = 1
        cupsmallgiven_location[customerclicked] = (customer1location[0]+customerclicked*(customer_size[0]+customer_inbetween_pix), (customer1location[1]+customer_size[1]-1))
        givennumbot[customerclicked] = cupnumbot
        givennumtop[customerclicked] = cupnumtop
        givenstrawnum[customerclicked], givenlidnum[customerclicked] = strawnum, lidnum
        giventapioca[customerclicked], givenice[customerclicked] = showtapioca, showice
        # start a countdown before showing the customer as happy or angry
        timecustserved[customerclicked] = pygame.time.get_ticks()
        # determine if the customer is satisfied or not
        if (surpriseme[customerclicked] and not (givennumbot[customerclicked],
                                         givennumtop[customerclicked],
                                         givenstrawnum[customerclicked],
                                         givenlidnum[customerclicked],
                                         giventapioca[customerclicked],
                                         givenice[customerclicked]) == gavesurprise[customerclicked] and \
            (random.random() > 0.15)) or \
            (givennumbot[customerclicked] == cupsmallnumbot[customerclicked] and \
                givennumtop[customerclicked] == cupsmallnumtop[customerclicked] and \
                    givenstrawnum[customerclicked] == smallstrawnum[customerclicked] and \
                        givenlidnum[customerclicked] == smalllidnum[customerclicked] and \
                            giventapioca[customerclicked] == smalltapioca[customerclicked] and \
                                givenice[customerclicked] == smallice[customerclicked]):
            happyorangry[customerclicked] = "happy"
            gavesurprise[customerclicked] = (0, 0, 0, 0, 0, 0)
            custwaiting[customerclicked] = 0 # the customer is satisfied so he is no longer waiting for his drink
        else:
            happyorangry[customerclicked] = "angry"
            if goalsmode or speedrun: angrycustcount += 1
            if surpriseme[customerclicked]: 
                gavesurprise[customerclicked] = (givennumbot[customerclicked],
                                                 givennumtop[customerclicked],
                                                 givenstrawnum[customerclicked],
                                                 givenlidnum[customerclicked],
                                                 giventapioca[customerclicked],
                                                 givenice[customerclicked])
    return showcupsmallgiven,custwaiting,cupsmallgiven_location,givennumbot,givennumtop, \
        givenstrawnum,giventapioca,timecustserved,happyorangry,gavesurprise,angrycustcount

def scale(thetuple):
    thetuple_scaled = tuple(ii*scaling_factor for ii in thetuple)
    return thetuple_scaled


                                                
# Set up the images on the screen 
bkdImg = pygame.image.load('bobagoround_backdroponly.png')
cuplargeemptyImg = pygame.image.load('bobagoround_cuplargeempty.png')
gray1Img = pygame.image.load('gray_1.png')
speedrunImg = pygame.image.load("bobagoround_speedrunbutton.png")
goalsImg = pygame.image.load("bobagoround_goalsbutton.png")
infiniteImg = pygame.image.load("bobagoround_infinitebutton.png")
goalsinstrImg = pygame.image.load("bobagoround_goalsinstructions.png")
daywonImg = pygame.image.load("bobagoround_daywon.png")
angryindgrayImg = pygame.image.load("bobagoround_angrycustindicator_gray.png")
angryindredImg = pygame.image.load("bobagoround_angrycustindicator_red.png")
goalstimerboxImg = pygame.image.load("bobagoround_timerbox.png")
counterImg = pygame.image.load("bobagoround_counter.png")
allgoalswonImg = pygame.image.load("bobagoround_allgoalswon.png")
phoneorderImg = pygame.image.load("bobagoround_phoneorder.png")
failedImg = pygame.image.load("bobagoround_failedscreen.png")
cupsmalliceImg = pygame.image.load("bobagoround_cupsmallice.png")
cupsmalltapiocaImg = pygame.image.load("bobagoround_cupsmalltapioca.png")
cupsurprisemeImg = pygame.image.load("bobagoround_cupsurpriseme.png")
requestbubbleImg = pygame.image.load("bobagoround_requestbubble.png")
highlightlidstrawImg = pygame.image.load("bobagoround_highlightlidstraw.png")
cuplargetapiocaImg = pygame.image.load("bobagoround_cuplargetapioca.png")
cuplargeicetopImg = pygame.image.load("bobagoround_cuplargeicetop.png")
cuplargeicemidImg = pygame.image.load("bobagoround_cuplargeicemid.png")
cuplargeicebottom = pygame.image.load("bobagoround_cuplargeicebottom.png")
ingredientsImg = pygame.image.load("bobagoround_ingredients.png")
speedrunstatsImg = pygame.image.load("bobagoround_speedrunstatstext.png")
exitbuttonImg = pygame.image.load("bobagoround_exitbutton.png")
statsimgsize = speedrunstatsImg.get_size()
maxpixtoadd = 20
pixelstoadd = [maxpixtoadd,maxpixtoadd,maxpixtoadd,maxpixtoadd,maxpixtoadd,maxpixtoadd]
custrisecountdown = 500 # ms
goalscash_locx, goalscash_locy = 111, 68
goalscash_loc = (goalscash_locx,goalscash_locy)
goalsangry_loc = (110, 89)
goalscashmade_locx, goalscashmade_locy = 114, 86
goalscashmade_loc = (goalscashmade_locx,goalscashmade_locy)
goalsdaynum_loc = (98,34)
showmodechoice = True
showcuplargeempty = False
showcuplarge = False
topchosen = False
bottomchosen = False
showtapioca = False
showice = False
highlightlid = False
highlightstraw = False
surpriseme = [False, False, False, False, False, False]
readyforrequest = True
showphoneorder = False
showdaywin = False
angrycustcount = 0
cupdrag = False
showrequest =    [0, 0, 0, 0, 0, 0]
custwaiting =    [0]*6
custstarttime =  [0, 0, 0, 0, 0, 0]
cupsmallnumtop = [0, 0, 0, 0, 0, 0]
cupsmallnumbot = [0, 0, 0, 0, 0, 0]
smallstrawnum =  [0, 0, 0, 0, 0, 0]
smalllidnum =    [0, 0, 0, 0, 0, 0]
smalltapioca =   [0, 0, 0, 0, 0, 0]
smallice =       [0, 0, 0, 0, 0, 0]
customeridnum =  [0, 0, 0, 0, 0, 0]
customerlocation =       [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
requestlocation =        [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
cupsmallgiven_location = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
showcupsmallgiven = [0, 0, 0, 0, 0, 0]
givennumbot =       [0, 0, 0, 0, 0, 0]
givennumtop =       [0, 0, 0, 0, 0, 0]
givenstrawnum =     [0, 0, 0, 0, 0, 0]
givenlidnum =       [0, 0, 0, 0, 0, 0]
giventapioca =      [0, 0, 0, 0, 0, 0]
givenice =          [0, 0, 0, 0, 0, 0]
timecustserved =    [0, 0, 0, 0, 0, 0]
gavesurprise = [(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0),]
happyorangry = ["", "", "", "", "", ""]

# clickable areas
waitfordepress = False

speedrunbuttonloc = (8,65)
speedrunbuttonsize = (62,14)
inbetweenbuttons_pix = 4
speedrunbuttonloc_scaled = scale(speedrunbuttonloc)
speedrunbuttonsize_scaled = scale(speedrunbuttonsize)
speedrunbuttonarea = pygame.Rect(speedrunbuttonloc_scaled, speedrunbuttonsize_scaled)
goalsbuttonloc = (speedrunbuttonloc[0]+speedrunbuttonsize[0]+inbetweenbuttons_pix,speedrunbuttonloc[1])
goalsbuttonsize = (39,14)
goalsbuttonloc_scaled = scale(goalsbuttonloc)
goalsbuttonsize_scaled = scale(goalsbuttonsize)
goalsbuttonarea = pygame.Rect(goalsbuttonloc_scaled, goalsbuttonsize_scaled)
infinitebuttonloc = (goalsbuttonloc[0]+goalsbuttonsize[0]+inbetweenbuttons_pix,speedrunbuttonloc[1])
infinitebuttonsize = (51,14)
infinitebuttonloc_scaled = scale(infinitebuttonloc)
infinitebuttonsize_scaled = scale(infinitebuttonsize)
infinitebuttonarea = pygame.Rect(infinitebuttonloc_scaled, infinitebuttonsize_scaled)

angrycustindicator_size = (5,9)

xtopleftingrs = 3
ytopleftingrs = 93
ingredients_square_sidelength = 21
gapingrsquares_pix = 1
# ingredient 1 mint tea
ingredient1rect = pygame.Rect((scaling_factor*xtopleftingrs, scaling_factor*ytopleftingrs), 
                              (scaling_factor*ingredients_square_sidelength, scaling_factor*ingredients_square_sidelength))
# ingredient 2 jasmine tea
ingredient2rect = pygame.Rect((scaling_factor*(xtopleftingrs+ingredients_square_sidelength+gapingrsquares_pix), scaling_factor*ytopleftingrs), 
                              (scaling_factor*ingredients_square_sidelength, scaling_factor*ingredients_square_sidelength))
# ingredient 3 peach tea
ingredient3rect = pygame.Rect((scaling_factor*xtopleftingrs, scaling_factor*(ytopleftingrs+ingredients_square_sidelength+gapingrsquares_pix)), 
                              (scaling_factor*ingredients_square_sidelength, scaling_factor*ingredients_square_sidelength))
# ingredient 4 tapioca
ingredient4rect = pygame.Rect((scaling_factor*(xtopleftingrs+ingredients_square_sidelength+gapingrsquares_pix), 
                               scaling_factor*(ytopleftingrs+ingredients_square_sidelength+gapingrsquares_pix)), 
                              (scaling_factor*ingredients_square_sidelength, scaling_factor*ingredients_square_sidelength))
# ingredient 5 taro tea
ingredient5rect = pygame.Rect((scaling_factor*(xtopleftingrs+2*ingredients_square_sidelength+2*gapingrsquares_pix), scaling_factor*ytopleftingrs), 
                              (scaling_factor*ingredients_square_sidelength, scaling_factor*ingredients_square_sidelength))
# ingredient 6 ice
ingredient6rect = pygame.Rect((scaling_factor*(xtopleftingrs+2*ingredients_square_sidelength+2*gapingrsquares_pix), 
                               scaling_factor*(ytopleftingrs+ingredients_square_sidelength+gapingrsquares_pix)), 
                              (scaling_factor*ingredients_square_sidelength, scaling_factor*ingredients_square_sidelength))
ingrs_rectslist = [ingredient1rect,ingredient2rect,ingredient3rect,ingredient4rect,ingredient5rect,ingredient6rect]
cuplargeposition_normal = ((xtopleftingrs+3*ingredients_square_sidelength+3*gapingrsquares_pix), ytopleftingrs)
cuplargeposition = cuplargeposition_normal
cuplargeposition_scaled = scale(cuplargeposition)
cuplarge_widthpix, cuplarge_heightpix = 33, 43
cuplargearea = pygame.Rect(cuplargeposition_scaled, (scaling_factor*cuplarge_widthpix,scaling_factor*cuplarge_heightpix))
cupcancelarea = pygame.Rect(scale((cuplargeposition[0]+cuplarge_widthpix-7, cuplargeposition[1]+cuplarge_heightpix-7)), scale((7,7)))
gapingramount_pix = 2
ingrsamount_locs =  [(xtopleftingrs+gapingramount_pix,ytopleftingrs+gapingramount_pix), 
                     (xtopleftingrs+ingredients_square_sidelength+gapingrsquares_pix+gapingramount_pix,ytopleftingrs+gapingramount_pix),
                     (xtopleftingrs+gapingramount_pix,ytopleftingrs+ingredients_square_sidelength+gapingrsquares_pix+gapingramount_pix),
                     (xtopleftingrs+ingredients_square_sidelength+gapingrsquares_pix+gapingramount_pix,
                      ytopleftingrs+ingredients_square_sidelength+gapingrsquares_pix+gapingramount_pix),
                     (xtopleftingrs+2*ingredients_square_sidelength+2*gapingrsquares_pix+gapingramount_pix,ytopleftingrs+gapingramount_pix),
                     (xtopleftingrs+2*ingredients_square_sidelength+2*gapingrsquares_pix+
                      gapingramount_pix,ytopleftingrs+ingredients_square_sidelength+gapingrsquares_pix+gapingramount_pix)]

lidstraw_square_sidelength = 10
xlids = (3+3*ingredients_square_sidelength+cuplarge_widthpix+4*1)
lid1location = (xlids, ytopleftingrs)
lid1location_scaled = scale(lid1location)
lid1rect = pygame.Rect(lid1location_scaled, (scaling_factor*lidstraw_square_sidelength,scaling_factor*lidstraw_square_sidelength))
lid2location = (xlids, (ytopleftingrs+lidstraw_square_sidelength+1))
lid2location_scaled = scale(lid2location)
lid2rect = pygame.Rect(lid2location_scaled, (scaling_factor*lidstraw_square_sidelength,scaling_factor*lidstraw_square_sidelength))
lid3location = (xlids, (ytopleftingrs+2*lidstraw_square_sidelength+2*1))
lid3location_scaled = scale(lid3location)
lid3rect = pygame.Rect(lid3location_scaled, (scaling_factor*lidstraw_square_sidelength,scaling_factor*lidstraw_square_sidelength))
lid4location = (xlids, (ytopleftingrs+3*lidstraw_square_sidelength+3*1))
lid4location_scaled = scale(lid4location)
lid4rect = pygame.Rect(lid4location_scaled, (scaling_factor*lidstraw_square_sidelength,scaling_factor*lidstraw_square_sidelength))

xstraws = (xlids+lidstraw_square_sidelength+1)
straw1location = (xstraws, ytopleftingrs)
straw1location_scaled = scale(straw1location)
straw1rect = pygame.Rect(straw1location_scaled, (scaling_factor*lidstraw_square_sidelength,scaling_factor*lidstraw_square_sidelength))
straw2location = (xstraws, (ytopleftingrs+lidstraw_square_sidelength+1))
straw2location_scaled = scale(straw2location)
straw2rect = pygame.Rect(straw2location_scaled, (scaling_factor*lidstraw_square_sidelength,scaling_factor*lidstraw_square_sidelength))
straw3location = (xstraws, (ytopleftingrs+2*lidstraw_square_sidelength+2*1))
straw3location_scaled = scale(straw3location)
straw3rect = pygame.Rect(straw3location_scaled, (scaling_factor*lidstraw_square_sidelength,scaling_factor*lidstraw_square_sidelength))
straw4location = (xstraws, (ytopleftingrs+3*lidstraw_square_sidelength+3*1))
straw4location_scaled = scale(straw4location)
straw4rect = pygame.Rect(straw4location_scaled, (scaling_factor*lidstraw_square_sidelength,scaling_factor*lidstraw_square_sidelength))

customer_size = (23, 20)
customer_inbetween_pix = 4
customer_size_scaled = scale(customer_size)
customer1location = (10, 37)
customer1location_scaled = scale(customer1location)
fullcustomers_width_scaled = scaling_factor*(6*customer_size[0]+5*customer_inbetween_pix)
fullcustomersrect_forserveclick = pygame.Rect(scale((10,2)),scale((6*customer_size[0]+5*customer_inbetween_pix, 85))) # if you click anywhere in here you are clicking a customer's face

phone_location = (152,93)
phone_size = (22,33)
phone_size_scaled = scale(phone_size)
phone_location_scaled = scale(phone_location)
phonerect = pygame.Rect(phone_location_scaled, phone_size_scaled)
order_ing1_location = (97,47)
order_ing_size = (21,29)
inbetweenorders_pix = 1
order_ing_size_scaled = scale(order_ing_size)
order_ing1_location_scaled = scale(order_ing1_location)
order_ing1_rect = pygame.Rect(order_ing1_location_scaled, order_ing_size_scaled)
order_ing2_location_scaled = tuple(ii*scaling_factor for ii in (order_ing1_location[0]+order_ing_size[0]+inbetweenorders_pix, order_ing1_location[1]))
order_ing2_rect = pygame.Rect(order_ing2_location_scaled, order_ing_size_scaled)
order_ing3_location_scaled = tuple(ii*scaling_factor for ii in (order_ing1_location[0], order_ing1_location[1]+order_ing_size[1]+inbetweenorders_pix))
order_ing3_rect = pygame.Rect(order_ing3_location_scaled, order_ing_size_scaled)
order_ing4_location_scaled = tuple(ii*scaling_factor for ii in (order_ing1_location[0]+order_ing_size[0]+inbetweenorders_pix, order_ing1_location[1]+order_ing_size[1]+inbetweenorders_pix))
order_ing4_rect = pygame.Rect(order_ing4_location_scaled, order_ing_size_scaled)
order_ing5_location_scaled = tuple(ii*scaling_factor for ii in (order_ing1_location[0]+2*order_ing_size[0]+2*inbetweenorders_pix, order_ing1_location[1]))
order_ing5_rect = pygame.Rect(order_ing5_location_scaled, order_ing_size_scaled)
order_ing6_location_scaled = tuple(ii*scaling_factor for ii in (order_ing1_location[0]+2*order_ing_size[0]+2*inbetweenorders_pix, order_ing1_location[1]+order_ing_size[1]+inbetweenorders_pix))
order_ing6_rect = pygame.Rect(order_ing6_location_scaled, order_ing_size_scaled)
orderingsrect_list = [order_ing1_rect,order_ing2_rect,order_ing3_rect,order_ing4_rect,order_ing5_rect,order_ing6_rect,]
phoneorderrect = pygame.Rect(tuple(ii*scaling_factor for ii in (88,45)), tuple(ii*scaling_factor for ii in (76,63)))

exitbutton_loc = (phone_location[0]-1, phone_location[1]+34)
exitbutton_location_scaled = scale(exitbutton_loc)
exitbutton_size_scaled = scale((24, 10))
exitbutton_rect = pygame.Rect(exitbutton_location_scaled,exitbutton_size_scaled)

textcash_locationright = (original_width-34, original_height-11) # use this to place object where you want
textcash_locationmid = (textcash_locationright[0]-4, textcash_locationright[1])
textcash_locationleft = (textcash_locationright[0]-8, textcash_locationright[1])

ingredient_price = 5

# Game variables
cashamount = 0
cashreceived = [False,False,False,False,False,False]
ingrs_amounts = [10]*6
ingrs_available = [True,True,True,True,True,True]

#No mode selected
speedrun = False
goalsmode = False
showgoalsinstructions = False
infinitemode = False
gamefailed = False
alreadywaited = False



################################# START RUN LOOP
startmintime, startextratime = 3, 14 # for speedrun: min 3 seconds, max 19 seconds between customers
countdown = (3 + random.choice(list(range(1,3))))*1000 # make the first countdown short-ish so we're not waiting years for 1st cust
running = True
while running:
    clock.tick(FPS)
    # dt = clock.tick(FPS) / 1000  # slows the computing to the given FPS (at most) and returns milliseconds 
                                 # between each call to 'tick'. Then convert time to seconds.
    # draw everything to original_screen, you will rescale at the end:
    original_screen.fill(BLACK)  # Fill the screen with background color.
    original_screen.blit(bkdImg,(0,0))
    for ingredienti in range(0,6,1): 
        if (ingrs_amounts[ingredienti]//10) != 0: 
            original_screen.blit(gray1Img,ingrsamount_locs[ingredienti]) # show the amounts of each ingredient
            original_screen.blit(pygame.image.load("gray_{0}.png".format(ingrs_amounts[ingredienti]%10)),(ingrsamount_locs[ingredienti][0]+2,ingrsamount_locs[ingredienti][1]))
        else: original_screen.blit(pygame.image.load("gray_{0}.png".format(ingrs_amounts[ingredienti]%10)),ingrsamount_locs[ingredienti])
    original_screen.blit(ingredientsImg,(0,0))
    if cashamount > 999: cashamount = 999
    original_screen.blit(pygame.image.load("green_{0}.png".format(cashamount%10)),textcash_locationright)
    if cashamount//100 != 0 or (cashamount//10)%10 != 0:
        original_screen.blit(pygame.image.load("green_{0}.png".format((cashamount//10)%10)),textcash_locationmid)
    if cashamount//100 != 0:
        original_screen.blit(pygame.image.load("green_{0}.png".format(cashamount//100)),textcash_locationleft)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user pressed the close button in the top corner of the window
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and cuplargearea.collidepoint(pygame.mouse.get_pos()) and \
             topchosen and highlightstraw and highlightlid and not cupcancelarea.collidepoint(pygame.mouse.get_pos()): 
                 # the large cup is ready and the player is clicking on it
             if event.button == 1:
                 if not waitfordepress:
                     cupdrag = True
                     waitfordepress = True
                     offset_x = cuplargearea.x - pygame.mouse.get_pos()[0]
                     offset_y = cuplargearea.y - pygame.mouse.get_pos()[1]
        elif event.type == pygame.MOUSEMOTION and cupdrag:
                cupdragx, cupdragy = pygame.mouse.get_pos()
                cuplargeposition = (int(cuplargeposition_normal[0] + (cupdragx + offset_x) 
                                        - 80)/scaling_factor, int(cuplargeposition_normal[1] + 
                                                                  (cupdragy + offset_y) - 80)/scaling_factor) 
                                                                  # the -80 is a temporary fix cuz I don't understand where it's coming from
        elif event.type == pygame.MOUSEBUTTONUP and cupdrag:
            cupdrag = False
            waitfordepress = False
            if any(showrequest) and fullcustomersrect_forserveclick.collidepoint(event.pos):
                numserved_start = showcupsmallgiven.count(1)
                custswaiting_start = custwaiting.count(1)
                showcupsmallgiven,custwaiting,cupsmallgiven_location,givennumbot,givennumtop, \
                    givenstrawnum,giventapioca,timecustserved,happyorangry,gavesurprise,angrycustcount = serve_customer(
                    customer1location_scaled,fullcustomers_width_scaled,
                    showrequest,topchosen,highlightstraw,highlightlid,
                    showcupsmallgiven,custwaiting,cupsmallgiven_location,givennumbot,
                    givennumtop,givenstrawnum,giventapioca,timecustserved,surpriseme,
                    givenice,gavesurprise,cupsmallnumbot,cupsmallnumtop,smallstrawnum,
                    smalllidnum,smalltapioca,smallice,happyorangry,goalsmode,speedrun,angrycustcount)
                numserved_end = showcupsmallgiven.count(1)
                custswaiting_end = custwaiting.count(1)
                if custswaiting_end<custswaiting_start or numserved_end > numserved_start:
                    # now that you gave the cup and know what you gave, the large cup is removed
                    showcuplarge, showcuplargeempty, showtapioca, showice, highlightlid, highlightstraw, topchosen, bottomchosen = remove_cup_large()
            cuplargeposition = cuplargeposition_normal
            # the servable cup is a unit made of: cuplarge_{}{}.png, largetapioca.png, largeicetop.png, largelid{}.png and largestraw{}.png
                
    
    
    
    
    ################################### HANDLE MOUSE PRESSES
    if waitfordepress:
        if not pygame.mouse.get_pressed()[0]: waitfordepress = False
    if pygame.mouse.get_pressed()[0] and not waitfordepress:
        waitfordepress = True
        if showmodechoice: 
            startmintime, startextratime = 3, 14 # reset the timer
            if speedrunbuttonarea.collidepoint(pygame.mouse.get_pos()):
                speedrun = True
                # start the timer
                lastcusttime = pygame.time.get_ticks()
                daystarttime = pygame.time.get_ticks()
            elif goalsbuttonarea.collidepoint(pygame.mouse.get_pos()):
                goalsmode = True
                showgoalsinstructions = True
                goals_profits_angry = [(50,10),(100,8),(150,5),(200,3)]
                goalsday, totalnumdays, goalsdayduration = 0, 4, 210 # seconds
            elif infinitebuttonarea.collidepoint(pygame.mouse.get_pos()):
                infinitemode = True
                # start the customer timer
                lastcusttime = pygame.time.get_ticks()
            showmodechoice = False
        elif showgoalsinstructions:
            showgoalsinstructions = False
            # start the timer & customer timer
            daystarttime = pygame.time.get_ticks() # returns the number of ms since pygame.init() was called
            lastcusttime = pygame.time.get_ticks()
        elif showdaywin:
            showgoalsinstructions = True
            showdaywin = False
            cashamount = 0 # now that you showed previous day's cash made, reset
        if cuplargearea.collidepoint(pygame.mouse.get_pos()):
            if not showcuplargeempty and not showcuplarge:
                showcuplargeempty = True
            elif cupcancelarea.collidepoint(pygame.mouse.get_pos()):
                # remove the cup, start from scratch
                showcuplarge, showcuplargeempty, showtapioca, showice, highlightlid, highlightstraw, topchosen, bottomchosen = remove_cup_large()
        elif ingredient4rect.collidepoint(pygame.mouse.get_pos()) and (showcuplargeempty or bottomchosen) and \
            ingrs_available[3] and not showtapioca: # tapioca balls
            showtapioca = True
            if not speedrun:
                ingrs_amounts[3] -= 1
                if ingrs_amounts[3] == 0: ingrs_available[3] = False
        elif ingredient6rect.collidepoint(pygame.mouse.get_pos()) and (showcuplargeempty or bottomchosen) and \
            ingrs_available[5] and not showice: # ice
            showice = True
            if not speedrun:
                ingrs_amounts[5] -= 1
                if ingrs_amounts[5] == 0: ingrs_available[5] = False
        elif lid1rect.collidepoint(pygame.mouse.get_pos()):
            highlightlid = True
            lidnum = 1
        elif lid2rect.collidepoint(pygame.mouse.get_pos()):
            highlightlid = True
            lidnum = 2
        elif lid3rect.collidepoint(pygame.mouse.get_pos()):
            highlightlid = True
            lidnum = 3
        elif lid4rect.collidepoint(pygame.mouse.get_pos()):
            highlightlid = True
            lidnum = 4
        elif straw1rect.collidepoint(pygame.mouse.get_pos()):
            highlightstraw = True
            strawnum = 1
        elif straw2rect.collidepoint(pygame.mouse.get_pos()):
            highlightstraw = True
            strawnum = 2
        elif straw3rect.collidepoint(pygame.mouse.get_pos()):
            highlightstraw = True
            strawnum = 3
        elif straw4rect.collidepoint(pygame.mouse.get_pos()):
            highlightstraw = True
            strawnum = 4
        elif phonerect.collidepoint(pygame.mouse.get_pos()):
            showphoneorder = True
        elif showphoneorder:
            if cashamount >= ingredient_price:
                for ingredienti in range(0,6,1):
                    if orderingsrect_list[ingredienti].collidepoint(pygame.mouse.get_pos()):
                        cashamount -= ingredient_price
                        showphoneorder = False
                        ingrs_amounts[ingredienti] += 10
                        ingrs_available[ingredienti] = True
                        if ingrs_amounts[ingredienti] > 19: ingrs_amounts[ingredienti] = 19
            if not phoneorderrect.collidepoint(pygame.mouse.get_pos()):
                    showphoneorder = False
        elif exitbutton_rect.collidepoint(pygame.mouse.get_pos()):
            showmodechoice = True
            # remove the cup, start from scratch
            showcuplarge, showcuplargeempty, showtapioca, showice, highlightlid, highlightstraw, topchosen, bottomchosen = remove_cup_large()
            speedrun = False
            goalsmode = False
            infinitemode = False
            cashamount = 0
            ingrs_amounts = [10]*6
            ingrs_available = [True,True,True,True,True,True]
            gamefailed = False
            showrequest = [0]*6
            custwaiting = [0]*6
            angrycustcount = 0
            showcupsmallgiven = [0]*6
        else:
            for ingredienti in range(0,6,1):
                if ingrs_rectslist[ingredienti].collidepoint(pygame.mouse.get_pos()) and \
                    (showcuplargeempty or bottomchosen) and ingrs_available[ingredienti] and \
                        not topchosen: 
                    showcuplargeempty = False
                    showcuplarge = True
                    if not speedrun:
                        ingrs_amounts[ingredienti] -= 1
                        if ingrs_amounts[ingredienti] == 0: ingrs_available[ingredienti] = False
                    if not bottomchosen and not ingredienti==5 and not ingredienti==3:
                        cupnumbot, cupnumtop, bottomchosen = ingredienti+1, 0, True
                    elif bottomchosen and not ingredienti==5 and not ingredienti==3:
                        cupnumtop, topchosen = ingredienti+1, True
        if any(showrequest) and fullcustomersrect_forserveclick.collidepoint(pygame.mouse.get_pos()):
            # there is at least one boba request and the player is clicking on a customer area
            showcupsmallgiven,custwaiting,cupsmallgiven_location,givennumbot,givennumtop, \
                givenstrawnum,giventapioca,timecustserved,happyorangry,gavesurprise,angrycustcount = serve_customer(customer1location_scaled,fullcustomers_width_scaled,
                                   showrequest,topchosen,highlightstraw,highlightlid,
                                   showcupsmallgiven,custwaiting,cupsmallgiven_location,givennumbot,
                                   givennumtop,givenstrawnum,giventapioca,timecustserved,surpriseme,
                                   givenice,gavesurprise,cupsmallnumbot,cupsmallnumtop,smallstrawnum,
                                   smalllidnum,smalltapioca,smallice,happyorangry,goalsmode,speedrun,
                                   angrycustcount)
            # now that you gave the cup and know what you gave, the large cup is removed
            showcuplarge, showcuplargeempty, showtapioca, showice, highlightlid, highlightstraw, topchosen, bottomchosen = remove_cup_large()
             
                       
            
    
    
    ######################### CHOOSE WHEN CUSTOMER appears and makes a request
    if not showmodechoice and not showgoalsinstructions and not showdaywin:
        timenow = pygame.time.get_ticks()
        timesincelastcust = timenow - lastcusttime
        if timesincelastcust >= countdown and not all(showrequest) and readyforrequest and not gamefailed:
            empty_indices  = [index for (index, item) in enumerate(showrequest) if item == 0]
            custlocationind = random.choice(empty_indices)
            showrequest[custlocationind] = 1
            custwaiting[custlocationind] = 1
            custstarttime[custlocationind] = pygame.time.get_ticks()
            if all(custwaiting) and speedrun: # if this was the last customer to make it full
                gamefailed = True
                timesurvived = (pygame.time.get_ticks() - daystarttime) / 1000
            surpriseme[custlocationind] = (random.random() > 0.9) # every tenth request is a surpriseme
            if not surpriseme[custlocationind]:
                cupsmallnumtop[custlocationind] = random.choice([1,2,3,5])
                cupsmallnumbot[custlocationind] = random.choice([1,2,3,5])
                smallstrawnum[custlocationind] = random.choice([1,2,3,4])
                smalllidnum[custlocationind] = random.choice([1,2,3,4])
                smalltapioca[custlocationind] = random.choice([0,1])
                smallice[custlocationind] = random.choice([0,1])
            
            requestlocation[custlocationind] = (customer1location[0]+custlocationind*(customer_size[0]+customer_inbetween_pix), 2)
            customeridnum[custlocationind] = random.choice([1,2,3,4,5,6,7,8,9])
            customerlocation[custlocationind] = (requestlocation[custlocationind][0], 37)
            readyforrequest = False # so it won't come back in this if until smth else makes this True
            if speedrun:
                if startmintime >= 0.8: startmintime -= 0.1 # never go below 700ms between custs
                if startextratime >= 3: startextratime -= 0.9
                countdown = (startmintime + random.choice(list(range(1,int(startextratime+1)))))*1000 
            elif goalsmode:
                countdown = (2 + random.choice(list(range(1,10))))*1000 # min 2 seconds, max 11 seconds between customers
                if goalsday == totalnumdays-1: # last day
                    countdown = countdown - 1.1
            else:
                countdown = (2.5 + random.choice(list(range(1,15))))*1000
            lastcusttime = timenow
        if timesincelastcust >= countdown and not all(showrequest) and not gamefailed: readyforrequest = True

    # Handle goals
    if goalsmode and not showgoalsinstructions and not showdaywin:
        runtime = pygame.time.get_ticks() - daystarttime
        if runtime > goalsdayduration*1000:
            if cashamount >= goals_profits_angry[goalsday][0] and angrycustcount < goals_profits_angry[goalsday][1]:
                # reset everything
                ingrs_amounts = [10]*6
                ingrs_available = [True,True,True,True,True,True]
                showrequest = [0]*6
                custwaiting = [0]*6
                showcupsmallgiven = [0]*6
                angrycustcount = 0
                showcuplarge = False
                showcuplargeempty = False
                # make it go to success screen 
                showdaywin = True
                alreadywaited = False
                # go to next day
                goalsday += 1
            else: gamefailed = True
    
    
    
    
    ################################ DRAW what needs to appear on the screen
    if showmodechoice:
        original_screen.blit(speedrunImg,speedrunbuttonloc)
        original_screen.blit(goalsImg,goalsbuttonloc)
        original_screen.blit(infiniteImg,infinitebuttonloc)
    elif showgoalsinstructions:
        original_screen.blit(goalsinstrImg,(0,0))
        numImg = pygame.image.load("goals_{0}.png".format(goalsday+1))
        imgwidth = numImg.get_size()[0]
        original_screen.blit(numImg,goalsdaynum_loc)
        show_numbers_in_font("goals", goals_profits_angry[goalsday][0], goalscash_loc, 1)
        original_screen.blit(pygame.image.load("goals_{0}.png".format(goals_profits_angry[goalsday][1])),goalsangry_loc)
    elif showdaywin:
        if goalsday == totalnumdays:
            original_screen.blit(allgoalswonImg,(0,0))
            show_numbers_in_font("goals", goals_profits_angry[goalsday-1][0], goalscash_loc, 1)
            show_numbers_in_font("goals", cashamount, goalscashmade_loc, 1)
        else:
            original_screen.blit(daywonImg,(0,0))
            numImg = pygame.image.load("goals_{0}.png".format(goalsday))
            imgwidth = numImg.get_size()[0]
            original_screen.blit(numImg,goalsdaynum_loc)
            show_numbers_in_font("goals", goals_profits_angry[goalsday-1][0], goalscash_loc, 1)
            show_numbers_in_font("goals", cashamount, goalscashmade_loc, 1)
    else:
        if goalsmode:
            for angrygoalcount in range(0,goals_profits_angry[goalsday][1],1):
                original_screen.blit(angryindgrayImg,(original_width-(6*(angrygoalcount+1))-1*angrygoalcount,1))
            if angrycustcount > 0: 
                for angrymadecount in range(0,angrycustcount,1):
                    original_screen.blit(angryindredImg,(original_width-(6*(angrymadecount+1))-1*angrymadecount,1))
                if angrycustcount == goals_profits_angry[goalsday][1]:
                    gamefailed = True
            # show the countdown
            original_screen.blit(goalstimerboxImg,(1,1))
            timenow = pygame.time.get_ticks()
            timeleft = int(goalsdayduration - ((timenow-daystarttime)/1000))
            if timeleft < 0: timeleft = 0
            show_numbers_in_font("gray",timeleft,(3,3),1)
        if any(showrequest):
            for ind, requestloctf in enumerate(showrequest):
                if requestloctf:
                    if pixelstoadd[ind] > 0: 
                        timesincecuststart = pygame.time.get_ticks() - custstarttime[ind]
                        pixelstoadd[ind] = int(maxpixtoadd *(1 - timesincecuststart/custrisecountdown))
                    original_screen.blit(pygame.image.load("bobagoround_customer{0}.png".format(customeridnum[ind])),(customerlocation[ind][0],customerlocation[ind][1]+pixelstoadd[ind]))
                    original_screen.blit(counterImg,(0,0))
                    original_screen.blit(pygame.image.load("customerpaws{0}.png".format(customeridnum[ind])),customerlocation[ind])
                    if pixelstoadd[ind] <= 0:
                        original_screen.blit(requestbubbleImg,requestlocation[ind])
                        if surpriseme[ind]:
                            original_screen.blit(cupsurprisemeImg,requestlocation[ind])
                        else:
                            original_screen.blit(pygame.image.load("bobagoround_cupsmall{0}{1}.png".format(cupsmallnumbot[ind],cupsmallnumtop[ind])),requestlocation[ind])
                            original_screen.blit(pygame.image.load("bobagoround_cupsmallstraw{0}.png".format(smallstrawnum[ind])),requestlocation[ind])
                            original_screen.blit(pygame.image.load("bobagoround_cupsmalllid{0}.png".format(smalllidnum[ind])),requestlocation[ind])
                            if smalltapioca[ind]:
                                original_screen.blit(cupsmalltapiocaImg,requestlocation[ind])
                            if smallice[ind]:
                                original_screen.blit(cupsmalliceImg,requestlocation[ind])
        if any(showcupsmallgiven):
            for ind, givenloctf in enumerate(showcupsmallgiven):
                if givenloctf:
                    original_screen.blit(pygame.image.load("bobagoround_cupsmall{0}{1}.png".format(givennumbot[ind],givennumtop[ind])),cupsmallgiven_location[ind])
                    original_screen.blit(pygame.image.load("bobagoround_cupsmallstraw{0}.png".format(givenstrawnum[ind])),cupsmallgiven_location[ind])
                    original_screen.blit(pygame.image.load("bobagoround_cupsmalllid{0}.png".format(givenlidnum[ind])),cupsmallgiven_location[ind])
                    if giventapioca[ind]:
                        original_screen.blit(cupsmalltapiocaImg,cupsmallgiven_location[ind])
                    if givenice[ind]:
                        original_screen.blit(cupsmalliceImg,cupsmallgiven_location[ind])
                    timenow = pygame.time.get_ticks()
                    timesinceserved = timenow - timecustserved[ind]
                    if happyorangry[ind] == "happy"  and not cashreceived[ind] and timesinceserved < 1000:
                        cashamount += 10
                        cashreceived[ind] = True
                    elif timesinceserved > 3.5*1000:
                        cashreceived[ind] = False
                        if happyorangry[ind] == "happy": #remove the customer, they are satisfied
                            showcupsmallgiven[ind] = 0
                            showrequest[ind] = 0
                            pixelstoadd[ind] = maxpixtoadd
                    elif timesinceserved >= 1*1000:
                        if happyorangry[ind] == "happy" and timesinceserved <= 2.75*1000:
                            original_screen.blit(pygame.image.load("bobagoround_customer{0}happy.png".format(customeridnum[ind])),customerlocation[ind])
                        elif happyorangry[ind] == "angry":
                            original_screen.blit(pygame.image.load("bobagoround_customer{0}angry.png".format(customeridnum[ind])),customerlocation[ind])
        if highlightstraw:
            strawlocs = (straw1location, straw2location, straw3location, straw4location)
            strawloc = strawlocs[strawnum-1]
            original_screen.blit(highlightlidstrawImg,strawloc)
        if highlightlid:
            lidlocs = (lid1location, lid2location, lid3location, lid4location)
            lidloc = lidlocs[lidnum-1]
            original_screen.blit(highlightlidstrawImg,lidloc)
        if showphoneorder:
            original_screen.blit(phoneorderImg,(0,0))
        # putting the cuplarge draws at the end so it flies above all else during drag
        if showcuplargeempty:
            original_screen.blit(cuplargeemptyImg,cuplargeposition)
        elif showcuplarge:
            original_screen.blit(pygame.image.load("bobagoround_cuplarge{0}{1}.png".format(cupnumbot,cupnumtop)),cuplargeposition)
        if showtapioca:
            original_screen.blit(cuplargetapiocaImg,cuplargeposition)
        if highlightlid:
            original_screen.blit(pygame.image.load("bobagoround_largelid{0}.png".format(lidnum)),cuplargeposition)
        if highlightstraw:
            original_screen.blit(pygame.image.load("bobagoround_largestraw{0}.png".format(strawnum)),(cuplargeposition[0]+14,cuplargeposition[1]-5))
        if showice:
            if showcuplargeempty:
                original_screen.blit(cuplargeicebottom,cuplargeposition)
            elif bottomchosen and not topchosen:
                original_screen.blit(cuplargeicemidImg,cuplargeposition)
            elif topchosen:
                original_screen.blit(cuplargeicetopImg,cuplargeposition)
        if gamefailed:
            original_screen.blit(failedImg,(0,0))
            if speedrun:
                speedrunstatstopleft = (32,90)
                original_screen.blit(speedrunstatsImg,speedrunstatstopleft)
                show_numbers_in_font("goals", timesurvived, (speedrunstatstopleft[0]+statsimgsize[0]+12,speedrunstatstopleft[1]), 1)
                show_numbers_in_font("goals", angrycustcount, (speedrunstatstopleft[0]+statsimgsize[0]+12, speedrunstatstopleft[1]+18), 1)
    original_screen.blit(exitbuttonImg,exitbutton_loc)
                

        
    ########################## RESCALE & DISPLAY
    fullwindow.blit(pygame.transform.scale(original_screen, fullwindow.get_rect().size), (0, 0))
    pygame.display.update()  # Or pygame.display.flip()
    if showdaywin and not alreadywaited:
        pygame.time.wait(700) # ms
        alreadywaited = True

exitgame()