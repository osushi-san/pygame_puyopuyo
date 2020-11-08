import sys
import pygame

pygame.init() 
screen = pygame.display.set_mode((1000, 1000)) 
pygame.display.set_caption("test")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()