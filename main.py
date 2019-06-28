import pygame, sys
from player import Player

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

TILEWIDTH = 40
TILEHEIGHT = 40

WINDOWWIDTH = 13*TILEWIDTH
WINDOWHEIGHT = 13*TILEHEIGHT

BACKGROUND = (107, 142, 35)

pygame.init()
s = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Bomberman')


clock = pygame.time.Clock()

player = Player()

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

block_img = pygame.image.load('images/terrain/block.png')
block_img = pygame.transform.scale(block_img, (TILEWIDTH, TILEHEIGHT))


def draw():
    s.fill(BACKGROUND)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                s.blit(block_img, (i*TILEWIDTH, j*TILEHEIGHT, TILEHEIGHT, TILEWIDTH))
    s.blit(player.animation[player.direction][player.frame],
           (player.posX*(TILEWIDTH/4), player.posY*(TILEHEIGHT/4), TILEWIDTH, TILEHEIGHT))

    pygame.display.update()


def main():
    while True:
        clock.tick(15)
        keys = pygame.key.get_pressed()

        temp = player.direction
        movement = False
        if keys[pygame.K_DOWN]:
            temp = 0
            # player.posY += 1
            player.move(0, 1, map)
            movement = True
        elif keys[pygame.K_RIGHT]:
            temp = 1
            # player.posX += 1
            player.move(1, 0, map)
            movement = True
        elif keys[pygame.K_UP]:
            temp = 2
            # player.posY -= 1
            player.move(0, -1, map)
            movement = True
        elif keys[pygame.K_LEFT]:
            temp = 3
            # player.posX -= 1
            player.move(-1, 0, map)
            movement = True
        if temp != player.direction:
            player.frame = 0
            player.direction = temp
        if movement:
            if player.frame == 2:
                player.frame = 0
            else:
                player.frame += 1
        draw()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)


main()
