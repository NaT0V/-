import pygame
import time
pygame.init()

win = pygame.display.set_mode((600,400))

color = (200,70,100)
win.fill(color)
dir_rect = "right"

i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    win.fill(color)

    if dir_rect == "right":
        i = i + 10
    elif dir_rect == "left":
        i = i - 10
    if i == 500:
        dir_rect = "left"
    if i == 0:
        dir_rect = "right"

    pygame.draw.rect(win,(0,0,0),(i,150,200,100))
    pygame.display.update()
    
         
    if dir_rect == "right":
        i = i + 10
    elif dir_rect == "left":
        i = i - 10
    if i == 320:
        dir_rect = "left"
    if i == 0:
        dir_rect = "right"
    pygame.draw.circle(win,(0,0,0),(200,i),70)
    pygame.display.update()
    time.sleep(0.05)
    
    
    
    
    

