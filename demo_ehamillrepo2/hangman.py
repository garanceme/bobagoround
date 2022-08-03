#variables
import pygame
import random
import re
newran = ''
word = ''
new = ''
guessct = 0

pygame.init()

#screen dimensions
screen = pygame.display.set_mode((800, 600))
#name/logo
pygame.display.set_caption("Hangman")
icon = pygame.image.load('51Wm6VppYEL.png')
pygame.display.set_icon(icon)
#colors
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
#hangman base
hangbase = pygame.image.load('attempt_hang_base.png')
hangbaseX = 217
hangbaseY = 60

#text
font = pygame.font.Font(None, 50)
texttop = font.render('select a difficulty', True, black)
textleft = font.render('easy', True, black)
textmid = font.render('medium', True, black)
textright = font.render('hard', True, black)

textA = font.render(' a ', True, black)
textB = font.render('b', True, black)
textC = font.render('c', True, black)
textD = font.render('d', True, black)
textE = font.render('e', True, black)
textF = font.render('f', True, black)
textG = font.render('g', True, black)
textH = font.render('h', True, black)
textI = font.render('i', True, black)
textJ = font.render('j', True, black)
textK = font.render('k', True, black)
textL = font.render('l', True, black)
textM = font.render('m', True, black)
textN = font.render('n', True, black)
textO = font.render('o', True, black)
textP = font.render('p', True, black)
textQ = font.render('q', True, black)
textR = font.render('r', True, black)
textS = font.render('s', True, black)
textT = font.render('t', True, black)
textU = font.render('u', True, black)
textV = font.render('v', True, black)
textW = font.render('w', True, black)
textX = font.render('x', True, black)
textY = font.render('y', True, black)
textZ = font.render('z', True, black)

        
#text dimensions
textRectop = texttop.get_rect()
textRectop.center = (800//2, 425)

textRecleft = textleft.get_rect()
textRecleft.center = (250, 475)

textRecmid = textmid.get_rect()
textRecmid.center = (800//2, 475)

textRecright = textright.get_rect()
textRecright.center = (550, 475)

recA = textA.get_rect()
recA.center = (250,405)

recB = textB.get_rect()
recB.center = (290,405)

recC = textC.get_rect()
recC.center = (330,405)

recD = textD.get_rect()
recD.center = (370,405)

recE = textE.get_rect()
recE.center = (410,405)

recF = textF.get_rect()
recF.center = (450,405)

recG = textG.get_rect()
recG.center = (490,405)

recH = textH.get_rect()
recH.center = (540,405)

recI = textI.get_rect()
recI.center = (290,455)

recJ = textJ.get_rect()
recJ.center = (330,455)

recK = textK.get_rect()
recK.center = (370,455)

recL = textL.get_rect()
recL.center = (410,455)

recM = textM.get_rect()
recM.center = (450,455)

recN = textN.get_rect()
recN.center = (490,455)

recO = textO.get_rect()
recO.center = (290,505)

recP = textP.get_rect()
recP.center = (330,505)

recQ = textQ.get_rect()
recQ.center = (370,505)

recR = textR.get_rect()
recR.center = (410,505)

recS = textS.get_rect()
recS.center = (450,505)

recT = textT.get_rect()
recT.center = (490,505)

recU = textU.get_rect()
recU.center = (290,555)

recV = textV.get_rect()
recV.center = (330,555)

recW = textW.get_rect()
recW.center = (370,555)

recX = textX.get_rect()
recX.center = (410,555)

recY = textY.get_rect()
recY.center = (450,555)

recZ = textZ.get_rect()
recZ.center = (490,555)





#hangman base function


def base():
    screen.blit(hangbase, (hangbaseX, hangbaseY))

def manhd():
    pygame.draw.circle(screen, black, (455, 230), 25, 5)

def manbody():
    pygame.draw.line(screen, black, (455, 255), (455, 310), 5)

def manarm1():
    pygame.draw.line(screen, black, (455, 278), (410, 260.3), 5)

def manarm2():
    pygame.draw.line(screen, black, (455, 278), (500, 260.3), 5)

def manleg1():
    pygame.draw.line(screen, black, (455, 310), (420, 350), 5)

def manleg2():
    pygame.draw.line(screen, black, (455, 310), (490, 350), 5)

#functions for easy, medium, difficult, and letters click detection
def difclicke():
    if pygame.mouse.get_pressed()[0] and pygame.Rect(textRecleft).collidepoint(pos):
        return True
    return False

def difclickm():
    if pygame.mouse.get_pressed()[0] and pygame.Rect(textRecmid).collidepoint(pos):
        return True
    return False

def difclickh():
    if pygame.mouse.get_pressed()[0] and pygame.Rect(textRecright).collidepoint(pos):
        return True
    return False

#funciton for reseting screen
def letters():
    screen.blit(textA, recA)
    screen.blit(textB, recB)
    screen.blit(textC, recC)
    screen.blit(textD, recD)
    screen.blit(textE, recE)
    screen.blit(textF, recF)
    screen.blit(textG, recG)
    screen.blit(textH, recH)
    screen.blit(textI, recI)
    screen.blit(textJ, recJ)
    screen.blit(textK, recK)
    screen.blit(textL, recL)
    screen.blit(textM, recM)
    screen.blit(textN, recN)
    screen.blit(textO, recO)
    screen.blit(textP, recP)
    screen.blit(textQ, recQ)
    screen.blit(textR, recR)
    screen.blit(textS, recS)
    screen.blit(textT, recT)
    screen.blit(textU, recU)
    screen.blit(textV, recV)
    screen.blit(textW, recW)
    screen.blit(textX, recX)
    screen.blit(textY, recY)
    screen.blit(textZ, recZ)
#function for selecting difficulty
#picks a random word and displays it as dashes
def selection():
    global newran
    global word
    screen.blit(texttop, textRectop)
    screen.blit(textleft, textRecleft)
    screen.blit(textmid, textRecmid)
    screen.blit(textright, textRecright)
    base()

    with open("wordlist.txt", 'r') as file:
        data = file.readlines()
        data = ''.join(data)

        if difclicke() == True:
            strl = ''
            wordlist = re.findall(r'\b[a-zA-Z]{4,5}\b',data) 
            word = (wordlist[random.randrange(len(wordlist))])
            rword = word
            new = list(rword)
            newran = ('_ ' * len(new))
            return (word)

        elif difclickm() == True:
            strl = ''
            wordlist = re.findall(r'\b[a-zA-Z]{6}\b',data) 
            word = (wordlist[random.randrange(len(wordlist))])
            rword = word
            new = list(rword)
            newran = ('_ ' * len(new))
            return (word)

        elif difclickh() == True:
            wordlist = re.findall(r'\b[a-zA-Z]{7}\b',data) 
            word = (wordlist[random.randrange(len(wordlist))])
            rword = word
            new = list(rword)
            newran = ('_ ' * len(new))
            return (word)
#guess function if letter is in the ran word it turns green and shows in the word, if its not it turns red and draws a part of the man
def guess():

    global word
    global newran
    global running
    global pos
    global guessct
    guessct = 0

    while running:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False

        print(word)
        screen.fill(white)
        font2 = pygame.font.Font(None, 90)
        newtxt = font2.render(str(newran), True, black)
        textRecran = newtxt.get_rect()
        textRecran.center = (800//2, 100)
        screen.blit(newtxt, textRecran)
        letters()
        base()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recA).collidepoint(pos):
                
            if 'a' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textA = font.render('a', True, green)
                    recA.center = (260,405)
                    screen.blit(textA, recA)
                    pygame.display.update()
                        

            elif 'a' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textA = font.render('a', True, red)
                    recA.center = (260,405)
                    screen.blit(textA, recA)
                    pygame.display.update()

                                            
        if pygame.mouse.get_pressed()[0] and pygame.Rect(recB).collidepoint(pos):

            if 'b' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textB = font.render('b', True, green)
                    screen.blit(textB, recB)
                    pygame.display.update()

            elif 'b' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textB = font.render('b', True, red)
                    screen.blit(textB, recB)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recC).collidepoint(pos):

            if 'c' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textC = font.render('c', True, green)
                    screen.blit(textC, recC)
                    pygame.display.update()

            elif 'c' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textC = font.render('c', True, red)
                    screen.blit(textC, recC)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recD).collidepoint(pos):

            if 'd' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False       
                    textD = font.render('d', True, green)
                    screen.blit(textD, recD)
                    pygame.display.update()

            elif 'd' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textD = font.render('d', True, red)
                    screen.blit(textD, recD)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recE).collidepoint(pos):

            if 'e' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textE = font.render('e', True, green)
                    screen.blit(textE, recE)
                    pygame.display.update()

            elif 'e' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textE = font.render('e', True, red)
                    screen.blit(textE, recE)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recF).collidepoint(pos):

            if 'f' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False

                    textF = font.render('f', True, green)
                    screen.blit(textF, recF)
                    pygame.display.update()

            elif 'f' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textF = font.render('f', True, red)
                    screen.blit(textF, recF)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recG).collidepoint(pos):

            if 'g' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False

                    textG = font.render('g', True, green)
                    screen.blit(textG, recG)
                    pygame.display.update()

            elif 'g' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textG = font.render('g', True, red)
                    screen.blit(textG, recG)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recH).collidepoint(pos):

            if 'h' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                            
                    textH = font.render('h', True, green)
                    screen.blit(textH, recH)
                    pygame.display.update()

            elif 'h' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textH = font.render('h', True, red)
                    screen.blit(textH, recH)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recI).collidepoint(pos):

            if 'i' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textI = font.render('i', True, green)
                    screen.blit(textI, recI)
                    pygame.display.update()

            elif 'i' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textI = font.render('i', True, red)
                    screen.blit(textI, recI)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recJ).collidepoint(pos):

            if 'j' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textJ = font.render('j', True, green)
                    screen.blit(textJ, recJ)
                    pygame.display.update()

            elif 'j' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textJ = font.render('j', True, red)
                    screen.blit(textJ, recJ)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recK).collidepoint(pos):

            if 'k' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textK = font.render('k', True, green)
                    screen.blit(textK, recK)
                    pygame.display.update()

            elif 'k' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textK = font.render('k', True, red)
                    screen.blit(textK, recK)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recL).collidepoint(pos):

            if 'l' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textL = font.render('l', True, green)
                    screen.blit(textL, recL)
                    pygame.display.update()

            elif 'l' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textL = font.render('l', True, red)
                    screen.blit(textL, recL)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recM).collidepoint(pos):

            if 'm' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textM = font.render('m', True, green)
                    screen.blit(textM, recM)
                    pygame.display.update()

            elif 'm' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textM = font.render('m', True, red)
                    screen.blit(textM, recM)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recN).collidepoint(pos):

            if 'n' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textN = font.render('n', True, green)
                    screen.blit(textN, recN)
                    pygame.display.update()

            elif 'n' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.Quit:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textN = font.render('n', True, red)
                    screen.blit(textN, recN)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recO).collidepoint(pos):

            if 'o' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textO = font.render('o', True, green)
                    screen.blit(textO, recO)
                    pygame.display.update()

            elif 'o' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textO = font.render('o', True, red)
                    screen.blit(textO, recO)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recP).collidepoint(pos):

            if 'p' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textP = font.render('p', True, green)
                    screen.blit(textP, recP)
                    pygame.display.update()

            elif 'p' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textP = font.render('p', True, red)
                    screen.blit(textP, recP)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recQ).collidepoint(pos):

            if 'q' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textQ = font.render('q', True, green)
                    screen.blit(textQ, recQ)
                    pygame.display.update()

            elif 'q' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textQ = font.render('q', True, red)
                    screen.blit(textQ, recQ)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recR).collidepoint(pos):

            if 'r' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textR = font.render('r', True, green)
                    screen.blit(textR, recR)
                    pygame.display.update()

            elif 'r' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textR = font.render('r', True, red)
                    screen.blit(textR, recR)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recS).collidepoint(pos):

            if 's' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textS = font.render('s', True, green)
                    screen.blit(textS, recS)
                    pygame.display.update()

            elif 's' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textS = font.render('s', True, red)
                    screen.blit(textS, recS)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recT).collidepoint(pos):

            if 't' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textT = font.render('t', True, green)
                    screen.blit(textT, recT)
                    pygame.display.update()

            elif 't' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textT = font.render('t', True, red)
                    screen.blit(textT, recT)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recU).collidepoint(pos):

            if 'u' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textU = font.render('u', True, green)
                    screen.blit(textU, recU)
                    pygame.display.update()

            elif 'u' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textU = font.render('u', True, red)
                    screen.blit(textU, recU)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recV).collidepoint(pos):

            if 'v' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textV = font.render('v', True, green)
                    screen.blit(textV, recV)
                    pygame.display.update()

            elif 'v' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textV = font.render('v', True, red)
                    screen.blit(textV, recV)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recW).collidepoint(pos):

            if 'w' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textW = font.render('w', True, green)
                    screen.blit(textW, recW)
                    pygame.display.update()

            elif 'w' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textW = font.render('w', True, red)
                    screen.blit(textW, recW)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recX).collidepoint(pos):

            if 'x' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textX = font.render('x', True, green)
                    screen.blit(textX, recX)
                    pygame.display.update()

            elif 'x' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textX = font.render('x', True, red)
                    screen.blit(textX, recX)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recY).collidepoint(pos):

            if 'y' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textY = font.render('y', True, green)
                    screen.blit(textY, recY)
                    pygame.display.update()

            elif 'y' not in word:
                guessct += 1
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textY = font.render('y', True, red)
                    screen.blit(textY, recY)
                    pygame.display.update()

        if pygame.mouse.get_pressed()[0] and pygame.Rect(recZ).collidepoint(pos):

            if 'z' in word:
                while running:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    textZ = font.render('z', True, green)
                    screen.blit(textZ, recZ)   
                    pygame.display.update()

            elif 'z' not in word:
                while running:
                    guessct += 1
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        if event.type == pygame.QUIT:
                            running = False
                    if guessct == 1:
                        manhd()
                    elif guessct == 2:
                        manbody()
                    elif guessct == 3:
                        manarm1()
                    elif guessct == 4:
                        manarm2()
                    elif guessct == 5:
                        manleg1()
                    elif guessct == 6:
                        manleg2()
                    textZ = font.render('z', True, red)
                    screen.blit(textZ, recZ)
                    pygame.display.update()



        pygame.display.update()
        
def game():
    while selection() == word:
        guess()
            


#main line    
running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
    game()
    pygame.display.update()

