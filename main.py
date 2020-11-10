import sys
import pygame

SIZE = 40
RGB_RED = (255, 0, 0)
RGB_YELLOW = (255, 255, 0)
RGB_BLUE = (0, 0, 255)
RGB_GREEN = (0, 255, 0)
RGB_WHITE = (255, 255, 255)
RGB_BLACK = (0, 0, 0)
BLACK = 0
RED = 1
YELLOW = 2
BLUE = 3
GREEN = 4
WHITE = 5

COLOR_DICT = {BLACK: RGB_BLACK,
              RED: RGB_RED,
              YELLOW: RGB_YELLOW,
              BLUE: RGB_BLUE,
              GREEN: RGB_GREEN,
              WHITE: RGB_WHITE,}

# methods
def draw_from_board(surface, board):
    for x in range(1, 7):
        for y in range(1, 13):
            if 1 <= board[x][y] <= 4:
                draw_puyo(surface, COLOR_DICT[board[x][y]], x, y)
            else:
                draw_puyo_frame(surface, x, y)

def draw_puyo(surface, color, x, y):
    x_center = int(SIZE * x - SIZE / 2)
    y_center = int(SIZE * (13 - y) - SIZE / 2)
    pygame.draw.circle(surface, color, (x_center, y_center), int(SIZE / 2))
    draw_puyo_frame(surface, x, y)

def draw_puyo_frame(surface, x, y):
    left_x = (x - 1) * SIZE
    upper_y = (12 - y) * SIZE
    rect = pygame.Rect(left_x, upper_y, SIZE, SIZE)
    pygame.draw.rect(surface, RGB_WHITE, rect, 1)

# prepare
pygame.init() 
surface = pygame.display.set_mode((6 * SIZE, 12 * SIZE)) 
pygame.display.set_caption("puyo")

# draw puyo
board = [[ 0 for i in range(0, 13)] for j in range(0, 7)] # 0 is dammy
board[1][2] = RED
board[1][3] = RED
board[1][8] = RED
board[2][2] = RED
board[1][1] = BLUE
board[2][1] = BLUE
board[2][3] = BLUE
board[3][2] = BLUE
board[3][1] = GREEN
board[3][3] = GREEN
board[4][2] = GREEN
board[5][2] = GREEN
board[4][1] = YELLOW
board[5][1] = YELLOW
board[5][3] = YELLOW
board[6][2] = YELLOW
board[4][3] = RED
board[5][4] = RED
board[6][1] = RED
board[6][3] = RED

draw_from_board(surface, board)

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()
