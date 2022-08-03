#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pygame button creation demo from:
https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/

Script created on Mon Jul  4 14:46:57 2022

@author: garance
"""

import pygame


# initializing the constructor
pygame.init()

# screen resolution
res = (720,720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255,255,255)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

color_change = (255,0,0)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

button_coords = [width/2,height/2,140,40]

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
text = smallfont.render('color' , True , color)

while True:
    
  # stores the (x,y) coordinates into
  # the variable as a tuple
  mouse = pygame.mouse.get_pos()
        
  # fills the screen with a color
  screen.fill((60,25,60))
  
  # if mouse is hovered on a button it
  # changes to lighter shade
  if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
    button = pygame.draw.rect(screen,color_light,button_coords)
    
  else:
    button = pygame.draw.rect(screen,color_dark,button_coords)
    
  for ev in pygame.event.get():
    
    if ev.type == pygame.QUIT:
      pygame.quit()
      
    #checks if a mouse is clicked
    if ev.type == pygame.MOUSEBUTTONDOWN:
      
      #if the mouse is clicked on the
      # button the game is terminated
      if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,color_change,button_coords)
    
    elif pygame.mouse.get_pressed()[0] and button.collidepoint(mouse):
        pygame.draw.rect(screen,color_change,button_coords)
  
  # superimposing the text onto our button
  screen.blit(text , (width/2+50,height/2))
  
  # updates the frames of the game
  pygame.display.update()
