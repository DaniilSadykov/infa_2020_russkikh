#Б02-010 Садыков Даниил, рефакторинг кода Русских Ивана

import pygame
from pygame.draw import *


def draw_bamboo_trees(x, y, sizex, sizey):
    
    '''
    x : x coordinate of top left point of the bottom reactangle in a base of a tree
    y : y coordinate of top left point of the bottom reactangle in a base of a tree
    sizex : width of the tree trunk or 1/16 of the whole width of the tree
    sizey : height of the tree trunk or 1/5 of the whole height of the tree 
    '''
    # building the base of a tree
    rect(screen, green, (x, y, sizex, sizey))
    rect(screen, green, (x, y-1.292*sizey, sizex, sizey*1.167))
    
    #bottom tilted block of bamboo
    stick1 = pygame.Surface((sizex*7/10, 3*sizey/4))
    stick1.fill(green)
    stick1.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick1, -20), (x-0.1*sizex, y-2.167*sizey))
    
    #top tilted block of bamboo
    stick2 = pygame.Surface((0.4286*sizex, sizey))
    stick2.fill(green)
    stick2.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick2, -20), (x+0.57*sizex, y-3.25*sizey))

    #left branches
    
    #top
    pygame.draw.arc(screen, green, (x-17.143*sizex, y-2.75*sizey, 17.143*sizex, 3.333*sizey), 0.4, 1.5, 2)
    #bottom
    pygame.draw.arc(screen, green, (x-11.143*sizex, y-1.57*sizey, 11.43*sizex, 3.333*sizey), 0.4, 1.5, 2)

    #right branches
    
    #top
    pygame.draw.arc(screen, green, (x+1.714*sizex, y-3.167*sizey, 17.143*sizex, 2.5*sizey), 1.7, 2.9, 2)
    #bottom
    pygame.draw.arc(screen, green, (x+1.014*sizex, y-1.867*sizey, 11.43*sizex, 2.5*sizey), 1.7, 2.9, 2)
    
    #leaves on the left branches
    leaf1 = pygame.Surface((2*sizex, sizey/10))
    leaf1.fill(peach)
    leaf1.set_colorkey(peach)
    pygame.draw.ellipse(leaf1, green, (0, 0, 2*sizex, sizey/10))\
        
    #top branch    
    screen.blit(pygame.transform.rotate(leaf1, -70), (x+4.86*sizex, y-2.89*sizey))
    screen.blit(pygame.transform.rotate(leaf1, -70), (x+6*sizex, y-2.94*sizey))
    screen.blit(pygame.transform.rotate(leaf1, -70), (x+6.57*sizex, y-3*sizey))
    screen.blit(pygame.transform.rotate(leaf1, -70), (x+7.143*sizex, y-3.05*sizey))
    screen.blit(pygame.transform.rotate(leaf1, -70), (x+7.714*sizex, y-3.0833*sizey))
    
    #bottom branch
    screen.blit(pygame.transform.rotate(leaf1, -70), (x+2.86*sizex, y-1.60*sizey))
    screen.blit(pygame.transform.rotate(leaf1, -70), (x+3.714*sizex, y-1.69*sizey))
    screen.blit(pygame.transform.rotate(leaf1, -70), (x+4.57*sizex, y-1.75*sizey))
    
    #leaves on the right branches
    leaf2 = pygame.Surface((2*sizex, 0.10833*sizey))
    leaf2.fill(peach)
    leaf2.set_colorkey(peach)
    pygame.draw.ellipse(leaf2, green, (0, 0, 2*sizex, 0.10833*sizey))
    
    #top
    screen.blit(pygame.transform.rotate(leaf2, 70), (x-7.7*sizex, y-2.7*sizey))
    screen.blit(pygame.transform.rotate(leaf2, 70), (x-7.143*sizex, y-2.7*sizey))
    screen.blit(pygame.transform.rotate(leaf2, 70), (x-6.6*sizex, y-2.6*sizey))
    screen.blit(pygame.transform.rotate(leaf2, 70), (x-6*sizex, y-2.55*sizey))
    screen.blit(pygame.transform.rotate(leaf2, 70), (x-4.86*sizex, y-2.456*sizey))
    
    #bottom 
    screen.blit(pygame.transform.rotate(leaf2, 70), (x-3.286*sizex, y-1.35*sizey))
    screen.blit(pygame.transform.rotate(leaf2, 70), (x-4*sizex, y-1.42*sizey))
    screen.blit(pygame.transform.rotate(leaf2, 70), (x-2.57*sizex, y-1.185*sizey))


def draw_panda(x, y, sizex, sizey):
    '''
    x : x coordinate of an origin point of body ellipse bounding reactangle
    y : y coordinate of an origin point of body ellipse bounding reactangle
    sizex : width of panda body
    sizey : height of panda body
    '''
    
    #body
    pygame.draw.ellipse(screen, white, (x , y+sizey/12, sizex, sizey))
    pygame.draw.ellipse(screen, black, (x-sizex/10, y+sizey/7, sizex/4, 15*sizey/13))
    
    #paws
    paw1 = pygame.Surface((sizex/200*54, sizey/130*75))
    paw1.fill(black)
    paw1.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(paw1, 10), (x, y+0.56*sizey))

    paw2 = pygame.Surface((sizex/200*40, sizey/130*80))
    paw2.fill(black)
    paw2.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(paw2, -20), (x, y+sizey))

    pygame.draw.rect(screen, black, (x+0.375*sizex, y+sizey/130*10, sizex/200*60, sizey/130*150))

    paw3 = pygame.Surface((sizex/200*48, sizey/130*75))
    paw3.fill(black)
    paw3.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(paw3, -15), (x+sizex*0.3, y+1.054*sizey))

    paw4 = pygame.Surface((sizex/2, 0.46*sizey))
    paw4.fill(peach)
    paw4.set_colorkey(peach)
    pygame.draw.ellipse(paw4, black, (0, 0, sizex/2, sizey/130*60))
    screen.blit(pygame.transform.rotate(paw4, 30), (x+0.15*sizex, y+1.23*sizey))

    pygame.draw.polygon(screen, black, [(x+0.65*sizex, y+sizey*1.07), (x+sizex/2, y+1.23*sizey), (x+0.65*sizex, y+sizey*1.46), (x+0.65*sizex, y+sizey*1.07)])

    paw5 = pygame.Surface((sizex*3/4, 0.54*sizey))
    paw5.fill(peach)
    paw5.set_colorkey(peach)
    pygame.draw.ellipse(paw5, black, (0, 0, sizex*3/4, 0.54*sizey))
    screen.blit(pygame.transform.rotate(paw5, 60), (x+0.45*sizex, y+0.7*sizey))
    
    #head with features
    face1 = pygame.Surface((0.85*sizex, 0.77*sizey))
    face1.fill(peach)
    face1.set_colorkey(peach)
    pygame.draw.ellipse(face1, white, (0, 0, 0.85*sizex, 0.77*sizey))
    screen.blit(pygame.transform.rotate(face1, 80), (x-0.15*sizex, y-0.46*sizey))

    face2 = pygame.Surface((0.85*sizex, 0.615*sizey))
    face2.fill(peach)
    face2.set_colorkey(peach)
    pygame.draw.ellipse(face2, white, (0, 0, 0.85*sizex, 0.615*sizey))
    screen.blit(pygame.transform.rotate(face1, -60), (x-sizex/20, y-0.53*sizey))

    face3 = pygame.Surface((0.75*sizex, 0.615*sizey))
    face3.fill(peach)
    face3.set_colorkey(peach)
    pygame.draw.ellipse(face3, white, (0, 0, 0.75*sizex, 0.615*sizey))
    screen.blit(pygame.transform.rotate(face3, 10), (x-0.09*sizex, y+0.192*sizey))

    ear1 = pygame.Surface((0.45*sizex, 0.346*sizey))
    ear1.fill(peach)
    ear1.set_colorkey(peach)
    pygame.draw.ellipse(ear1, black, (0, 0, 0.4*sizex, 0.307*sizey))
    screen.blit(pygame.transform.rotate(ear1, 55), (x-0.215*sizex, y-0.46*sizey))

    ear2 = pygame.Surface((0.4*sizex, 0.346*sizey))
    ear2.fill(peach)
    ear2.set_colorkey(peach)
    pygame.draw.ellipse(ear2, black, (0, 0, 0.4*sizex, 0.307*sizey))
    screen.blit(pygame.transform.rotate(ear2, -65), (x+0.3*sizex, y-0.37*sizey))

    pygame.draw.ellipse(screen, black, (x-sizex/40, y+0.73*sizey, sizex/5, sizey*0.192))

    pygame.draw.ellipse(screen, black, (x-sizex/10, y+0.307*sizey, 0.15*sizex, 0.346*sizey))

    pygame.draw.ellipse(screen, black, (x+sizex*0.15, y+0.385*sizey, sizex/5, 0.307*sizey))

    pygame.draw.rect(screen, black, (x+0.6*sizex, y+0.115*sizey, sizex*0.075, 0.692*sizey))



def draw_panda_child(x, y, sizex, sizey):
    '''
    x : x coordinate of an origin point of body ellipse bounding reactangle
    y : y coordinate of an origin point of body ellipse bounding reactangle
    sizex : width of panda child body
    sizey : height of panda child body
    '''
    
    #body
    pygame.draw.ellipse(screen, white, (x, y+sizey/12, sizex, sizey))
    
    #paws
    paw1 = pygame.Surface((0.35*sizex, 1.077*sizey))
    paw1.fill(peach)
    paw1.set_colorkey(peach)
    pygame.draw.ellipse(paw1, black, (0, 0, 0.4*sizex, 1.077*sizey))
    screen.blit(pygame.transform.rotate(paw1, -50), (x+0.05*sizex, y+0.384*sizey))

    paw2 = pygame.Surface((0.2*sizex, sizey*0.615))
    paw2.fill(black)
    paw2.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(paw2, -20), (x-0.12*sizex, y+0.46*sizey))

    paw3 = pygame.Surface((0.3*sizex, 0.307*sizey))
    paw3.fill(peach)
    paw3.set_colorkey(peach)
    pygame.draw.ellipse(paw3, black, (0, 0, 0.3*sizex, 0.307*sizey))
    screen.blit(pygame.transform.rotate(paw3, -50), (x-0.15*sizex, y+0.84*sizey))

    paw4 = pygame.Surface((sizex/2, 0.615*sizey))
    paw4.fill(peach)
    paw4.set_colorkey(peach)
    pygame.draw.ellipse(paw4, black, (0, -10, sizex/2, 0.615*sizey))
    screen.blit(pygame.transform.rotate(paw4, 60), (x+0.65*sizex, y+0.46*sizey))
    
    #head with features
    face1 = pygame.Surface((0.85*sizex, 0.7692*sizey))
    face1.fill(peach)
    face1.set_colorkey(peach)
    pygame.draw.ellipse(face1, white, (0, 0, 0.85*sizex, 0.7692*sizey))
    screen.blit(pygame.transform.rotate(face1, 80), (x-sizex/10, y-0.492*sizey))

    face2 = pygame.Surface((0.85*sizex, 0.6154*sizey))
    face2.fill(peach)
    face2.set_colorkey(peach)
    pygame.draw.ellipse(face2, white, (0, 0, 0.85*sizex, 0.6154*sizey))
    screen.blit(pygame.transform.rotate(face1, -60), (x-0.05*sizex, y-0.5846*sizey))

    face3 = pygame.Surface((0.75*sizex, 0.615*sizey))
    face3.fill(peach)
    face3.set_colorkey(peach)
    pygame.draw.ellipse(face3, white, (0, 0, 0.75*sizex, 0.615*sizey))
    screen.blit(pygame.transform.rotate(face3, 10), (x-0.05*sizex, y+0.154*sizey))

    ear1 = pygame.Surface((0.45*sizex, 0.34*sizey))
    ear1.fill(peach)
    ear1.set_colorkey(peach)
    pygame.draw.ellipse(ear1, black, (0, 0, 0.4*sizex, 0.307*sizey))
    screen.blit(pygame.transform.rotate(ear1, 55), (x-0.15*sizex, y-0.585*sizey))

    ear2 = pygame.Surface((0.4*sizex, 0.34*sizey))
    ear2.fill(peach)
    ear2.set_colorkey(peach)
    pygame.draw.ellipse(ear2, black, (0, 0, 0.4*sizex, 0.307*sizey))
    screen.blit(pygame.transform.rotate(ear2, -65), (x+0.3*sizex, y-0.46*sizey))

    pygame.draw.ellipse(screen, black, (x+0.02*sizex, y+0.615*sizey, 0.2*sizex, 0.23*sizey))

    pygame.draw.ellipse(screen, black, (x-0.05*sizex, y+0.154*sizey, 0.15*sizex, 0.34*sizey))

    pygame.draw.ellipse(screen, black, (x+0.2*sizex, y+0.23*sizey, 0.2*sizex, 0.307*sizey))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((1050, 700))

black = (0, 0, 0)
peach = (255, 175, 128)
green = (0, 104, 55)
white = (255, 255, 255)

screen.fill(peach)

draw_bamboo_trees(600, 400, 30, 120)
draw_bamboo_trees(900, 300, 40, 160)
draw_bamboo_trees(360, 570, 20, 85)
draw_bamboo_trees(150, 500, 24, 96)
draw_panda(700, 450, 200, 130)
draw_panda_child(450, 520, 100, 65)
draw_panda(-300, 250, 500, 325)

'''
Таким образом благодаря строкам чуть выше можно легко множить панд и деревья,
а также менять их местоположение и размер 

'''



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()