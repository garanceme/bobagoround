"""
Found on:
https://github.com/Kachornpat/Sudoku_PCA/tree/510217d62a6cd436f0291d654f256c91a24c8bdd
"""

import pygame
import sys

pygame.init()

#set window
screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Sudoku")
img = pygame.image.load("sudoku_img.png")
pygame.display.set_icon(img)

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
dark_gray = (225, 225, 225)

sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

enable_row = 0
enable_column = 0
enable = False

value = ""
font = pygame.font.SysFont("Ariel.ttf", 50)
number = None
       
#build white screen
screen.fill(white)


def table(pos, dimension, color):
   for i in range(3):
      for j in range(3):
         pygame.draw.rect(screen, color,
                          (pos[0] + dimension*i, pos[1] + dimension*j, dimension, dimension), 3)

def update(value):
   global number, enable_row, enable_column 
   pygame.draw.rect(screen, dark_gray, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
   number = font.render(f"{value}", True, black)
   screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
   sudoku[enable_column - 1][enable_row - 1] = value
   pygame.display.update()
   pygame.time.wait(100)

         
# draw small 3x3 table 9 times

for i in range(3):
   for j in range(3):
      table((50 + 150*i, 50 + 150*j), 50, gray)

# draw 3x3 one time
table((50, 50), 150, black)

#write the number
for i in range(9):
   for j in range(9):
      if sudoku[i][j] != 0:
         number = font.render(f"{sudoku[i][j]}", True, black)
         screen.blit(number, ((j + 1)*50 + 15, (i + 1)*50 + 10))
number = None
font2 = pygame.font.SysFont("Ariel.ttf", 30)
text = font2.render('Press "r" to run solver', True, black)
screen.blit(text, (535, 100))

# update screen
pygame.display.update()
run = True
def main(run):
   global enable, enable_row, enable_column, white, black, gray, dark_gray, sudoku, screen, number
   while run:
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
            
      if pygame.mouse.get_pressed()[0]:
         if enable == False:
            #enable box
            if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 500:
               #unhighlight previous box
               pygame.draw.rect(screen, white, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
               #highlisght new box
               pygame.draw.rect(screen,dark_gray,
                                ((pygame.mouse.get_pos()[0]//50)*50 + 2,
                                 (pygame.mouse.get_pos()[1]//50)*50 + 2, 46, 46))
               #write number on previous box
               if number != None and sudoku[enable_column-1][enable_row-1] != 0:
                  number = font.render(f"{sudoku[enable_column-1][enable_row-1]}", True, black)
                  screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
               #write number on new box
               if sudoku[(pygame.mouse.get_pos()[1]//50)-1][(pygame.mouse.get_pos()[0]//50)-1] != 0:
                  number = font.render(f"{sudoku[(pygame.mouse.get_pos()[1]//50)-1][(pygame.mouse.get_pos()[0]//50)-1]}", True, black)
                  screen.blit(number, ((pygame.mouse.get_pos()[0]//50)*50 + 15, (pygame.mouse.get_pos()[1]//50)*50 + 10))
               #update the enable box
               enable_row = (pygame.mouse.get_pos()[0]//50)
               enable_column = (pygame.mouse.get_pos()[1]//50)

               enable = True

         elif enable == True:
            if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 500:
               # for disable box
               if enable_row == pygame.mouse.get_pos()[0]//50 and enable_column == pygame.mouse.get_pos()[1]//50:
                  pygame.draw.rect(screen, white, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
                  if number != None and sudoku[enable_column-1][enable_row-1] != 0:
                     number = font.render(f"{sudoku[enable_column-1][enable_row-1]}", True, black)
                     screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
                  enable = False
               # enable another box from previous one
               else:
                     #unhighlight old box
                  pygame.draw.rect(screen, white, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
                  if number != None and sudoku[enable_column-1][enable_row-1] != 0:
                     number = font.render(f"{sudoku[enable_column-1][enable_row-1]}", True, black)
                     screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
                  
                  #highlight new box
                  pygame.draw.rect(screen,dark_gray,
                                 ((pygame.mouse.get_pos()[0]//50)*50 + 2,
                                    (pygame.mouse.get_pos()[1]//50)*50 + 2, 46, 46))
                  if number != None and sudoku[(pygame.mouse.get_pos()[1]//50)-1][(pygame.mouse.get_pos()[0]//50)-1] != 0:
                     number = font.render(f"{sudoku[(pygame.mouse.get_pos()[1]//50) - 1][ (pygame.mouse.get_pos()[0]//50) - 1]}", True, black)
                     screen.blit(number, ( (pygame.mouse.get_pos()[0]//50)*50 + 15, (pygame.mouse.get_pos()[1]//50)*50 + 10) )
                  #update the enable box
                  enable_row = (pygame.mouse.get_pos()[0]//50)
                  enable_column = (pygame.mouse.get_pos()[1]//50)
         
         pygame.display.update()
         pygame.time.wait(300)
         
      if enable == True:
         if pygame.key.get_pressed()[pygame.K_KP1] or pygame.key.get_pressed()[pygame.K_1]:
            update(1)  
         elif pygame.key.get_pressed()[pygame.K_KP2] or pygame.key.get_pressed()[pygame.K_2]:
            update(2)
         elif pygame.key.get_pressed()[pygame.K_KP3] or pygame.key.get_pressed()[pygame.K_3]:
            update(3)
         elif pygame.key.get_pressed()[pygame.K_KP4] or pygame.key.get_pressed()[pygame.K_4]:
            update(4)
         elif pygame.key.get_pressed()[pygame.K_KP5] or pygame.key.get_pressed()[pygame.K_5]:
            update(5)
         elif pygame.key.get_pressed()[pygame.K_KP6] or pygame.key.get_pressed()[pygame.K_6]:
            update(6)
         elif pygame.key.get_pressed()[pygame.K_KP7] or pygame.key.get_pressed()[pygame.K_7]:
            update(7)
         elif pygame.key.get_pressed()[pygame.K_KP8] or pygame.key.get_pressed()[pygame.K_8]:
            update(8)
         elif pygame.key.get_pressed()[pygame.K_KP9] or pygame.key.get_pressed()[pygame.K_9]:
            update(9)
         elif pygame.key.get_pressed()[pygame.K_BACKSPACE] or pygame.key.get_pressed()[pygame.K_DELETE]: 
            pygame.draw.rect(screen, dark_gray, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
            sudoku[enable_column - 1][enable_row - 1] = 0
            pygame.display.update()
            pygame.time.wait(100)
      if pygame.key.get_pressed()[pygame.K_r]:
         run = False
         if enable == True:
            pygame.draw.rect(screen, white, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
            if number != None and sudoku[enable_column-1][enable_row-1] != 0:
               number = font.render(f"{sudoku[enable_column-1][enable_row-1]}", True, black)
               screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         pygame.time.wait(100)
         
def valid(n, x, y):
   global sudoku
   for v in sudoku:
      if v[x] == n:
         return False
   for i in sudoku[y]:
      if i == n:
         return False
   for j in range(3):
      for k in range(3):
         if sudoku[(y // 3)*3 + j][(x // 3)*3 + k] == n:
            return False
   return True
        
def solve():
   global sudoku
   for i in range(9):
      for j in range(9):
         if sudoku[i][j] == 0:
            for n in range(1, 10):
               if valid(n, j, i):
                  sudoku[i][j] = n
                  pygame.draw.rect(screen, white, ((j+1)*50 + 2, (i+1)*50 + 2, 46, 46))
                  number = font.render(f"{n}", True, gray)
                  screen.blit(number, ((j+1)*50 + 15, (i+1)*50 + 10))
                  pygame.display.update()
                  if solve() == False:
                     sudoku[i][j] = 0
                     pygame.draw.rect(screen, white, ((j+1)*50 + 2, (i+1)*50 + 2, 46, 46))
                     pygame.display.update()
                  else:
                     return True
            return False

main(run)
p = pygame.time.get_ticks()
solve()
t = pygame.time.get_ticks()
n = t - p
print(n/1000, "seconds")
run = True
while True: 
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
