import pygame

width = 300
height = 300
bg_color = 255, 255, 255


screen = pygame.display.set_mode((width, height))
Title = pygame.display.set_caption("TicTacToe")
screen.fill(bg_color)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False