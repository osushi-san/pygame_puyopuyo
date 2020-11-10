import sys
import pygame

SIZE = 40
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# methods 
def draw_puyo(surface, color, x, y):
    x_center = int(SIZE * x - SIZE / 2)
    y_center = int(SIZE * (13 - y) - SIZE / 2)
    pygame.draw.circle(surface, color, (x_center, y_center), int(SIZE / 2))
    draw_puyo_frame(surface, x, y)

def draw_puyo_frame(surface, x, y):
    left_x = (x - 1) * SIZE
    upper_y = (12 - y) * SIZE
    rect = pygame.Rect(left_x, upper_y, SIZE, SIZE)
    pygame.draw.rect(surface, WHITE, rect, 1)

# prepare
pygame.init() 
surface = pygame.display.set_mode((6 * SIZE, 12 * SIZE)) 
pygame.display.set_caption("puyo")

# draw white frame
for x in range(1, 7):
    for y in range(1, 13):
        print(x, y)
        draw_puyo_frame(surface,x, y)

# draw puyo
draw_puyo(surface, RED, 1, 2)
draw_puyo(surface, RED, 1, 3)
draw_puyo(surface, RED, 1, 5)
draw_puyo(surface, RED, 2, 2)
draw_puyo(surface, BLUE, 1, 1)
draw_puyo(surface, BLUE, 2, 1)
draw_puyo(surface, BLUE, 2, 3)
draw_puyo(surface, BLUE, 3, 2)
draw_puyo(surface, GREEN, 3, 1)
draw_puyo(surface, GREEN, 3, 3)
draw_puyo(surface, GREEN, 4, 2)
draw_puyo(surface, GREEN, 5, 2)
draw_puyo(surface, YELLOW, 4, 1)
draw_puyo(surface, YELLOW, 5, 1)
draw_puyo(surface, YELLOW, 5, 3)
draw_puyo(surface, YELLOW, 6, 2)
draw_puyo(surface, RED, 4, 3)
draw_puyo(surface, RED, 5, 4)
draw_puyo(surface, RED, 6, 1)
draw_puyo(surface, RED, 6, 3)

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()