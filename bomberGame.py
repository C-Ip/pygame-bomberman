#!/usr/bin/python3

'''
File: Bomber Game

By: Calvin Ip
Last revised: 4/14/18

Bomber man lookalike game.

'''

import sys, os, pygame, random
from pygame.locals import *

def main():
    pygame.init()

    # Game dimensions
    TILESIZE = 50
    MAPWIDTH = 16
    MAPHEIGHT = 14
    
    # Color constants
    ROAD = pygame.image.load('road.png')
    WALL = pygame.image.load('wall.png')

    # List of road and wall
    street = [ROAD, WALL]

    tilemap = [[ROAD for width in range(MAPWIDTH)] for height in range(MAPHEIGHT)]
    tileValueList = [[0 for width in range(MAPWIDTH)] for height in range(MAPHEIGHT)]

    # Randomly add a wall if random number is greater than or equal to 8
    for rw in range(MAPHEIGHT):
        for cl in range(MAPWIDTH):
            randomNumber = random.randint(0, 10)
            if randomNumber >= 8:
                tile = WALL
                tileType = 1
                tileValue = 1
            else:
                tile = ROAD
                tileValue = 0
            tilemap[rw][cl] = tile
            tileValueList[rw][cl] = tileValue
    print(tileValueList)

    DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
    PLAYER1 = pygame.image.load('player1.png')
    PLAYER2 = pygame.image.load('player2.png')
    playerPosition1 = [0,0]
    playerPosition2 = [1, 1]

    # Game Loop

    while True:
        # All game events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:

                # Keys for player1
                if event.key == K_DOWN and playerPosition1[1] < MAPHEIGHT - 1 :
                    playerPosition1[1] += 1
                    # Check collisions
                    if playerPosition1 == playerPosition2 or tileValueList[playerPosition1[1]][playerPosition1[0]] == 1:
                        playerPosition1[1] -= 1
                        
                if event.key == K_UP and playerPosition1[1] > 0:
                    playerPosition1[1] -= 1
                    if playerPosition1 == playerPosition2 or tileValueList[playerPosition1[1]][playerPosition1[0]] == 1:
                        playerPosition1[1] += 1
                        
                if event.key == K_RIGHT and playerPosition1[0] < MAPWIDTH - 1:
                    playerPosition1[0] += 1
                    if playerPosition1 == playerPosition2 or tileValueList[playerPosition1[1]][playerPosition1[0]] == 1:
                        playerPosition1[0] -= 1
                        
                if event.key == K_LEFT and playerPosition1[0] > 0:
                    playerPosition1[0] -= 1
                    if playerPosition1 == playerPosition2 or tileValueList[playerPosition1[1]][playerPosition1[0]] == 1:
                        playerPosition1[0] += 1

                # Keys for player2
                if event.key == K_s and playerPosition2[1] < MAPHEIGHT - 1:
                    playerPosition2[1] += 1
                    if playerPosition2 == playerPosition1 or tileValueList[playerPosition2[1]][playerPosition2[0]] == 1:
                        playerPosition2[1] -= 1
                        
                if event.key == K_w and playerPosition2[1] > 0:
                    playerPosition2[1] -= 1
                    if playerPosition2 == playerPosition1 or tileValueList[playerPosition2[1]][playerPosition2[0]] == 1:
                        playerPosition2[1] += 1
                        
                if event.key == K_d and playerPosition2[0] < MAPWIDTH - 1:
                    playerPosition2[0] += 1
                    if playerPosition2 == playerPosition1 or tileValueList[playerPosition2[1]][playerPosition2[0]] == 1:
                        playerPosition2[0] -= 1
                        
                if event.key == K_a and playerPosition2[0] > 0:
                    playerPosition2[0] -= 1
                    if playerPosition2 == playerPosition1 or tileValueList[playerPosition2[1]][playerPosition2[0]] == 1:
                        playerPosition2[0] += 1

        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURF.blit(tilemap[row][column], (column*TILESIZE, row*TILESIZE))
                DISPLAYSURF.blit(PLAYER1,(playerPosition1[0]*TILESIZE, playerPosition1[1]*TILESIZE))
                DISPLAYSURF.blit(PLAYER2,(playerPosition2[0]*TILESIZE, playerPosition2[1]*TILESIZE))
                
        pygame.display.update()

if __name__ == '__main__':
    main()
