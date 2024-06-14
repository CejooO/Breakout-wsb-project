import sys
from random import randint
import pygame

WINDOW_SIZE = 600
ROWS = 2
COLS = 10
RECT_WIDTH = 75
RECT_HEIGHT = WINDOW_SIZE / (ROWS * COLS)
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20
PLAYER_SPEED = 5
GAP = 5

ball_radius = 10

rect_x = (WINDOW_SIZE - PLAYER_WIDTH) // 2
rect_y = (WINDOW_SIZE - PLAYER_HEIGHT) - 10

ball_x = WINDOW_SIZE // 2
ball_y = WINDOW_SIZE // 2

ball_speed_x = 3
ball_speed_y = 3

background_color = (0, 0, 0)
object_color = (255, 100, 255)
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Breakout')
clock = pygame.time.Clock()

list_of_blocks = []
ball = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)


def lose():
    global running
    if ball_y > WINDOW_SIZE + ball_radius:
       running = False

def create_blocks():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * (RECT_WIDTH + GAP)
            y = row * (RECT_HEIGHT + GAP)
            if col == 0:
                x += 2.5
            list_of_blocks.append(pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT))


def draw_blocks():
    for element in list_of_blocks:
        pygame.draw.rect(screen, object_color, element)


create_blocks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        rect_x += PLAYER_SPEED

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WINDOW_SIZE:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    if (rect_y <= ball_y + ball_radius <= rect_y + RECT_HEIGHT and
            rect_x <= ball_x <= rect_x + RECT_WIDTH):
        ball_speed_y = -ball_speed_y

    for block in list_of_blocks:
        if block.colliderect(ball):
            if randint(0, 1) == 1:
                ball_speed_x = -ball_speed_x
            ball_speed_y = -ball_speed_y
            list_of_blocks.remove(block)

    rect_x = max(0, min(rect_x, WINDOW_SIZE - RECT_WIDTH))

    screen.fill(background_color)
    draw_blocks()
    lose()
    ball = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)
    pygame.draw.rect(screen, object_color, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(screen, object_color, ball)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()
