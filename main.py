import pygame
from game.player import Player
from game.level import Level

pygame.init()
print("Pygame initialized")

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Broken Streets")
print("Window created")

clock = pygame.time.Clock()

player = Player(100, 500)
level = Level()

running = True
print("Entering game loop")

while running:
    screen.fill((0, 0, 0))  # black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event detected")
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    level.draw(screen)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Exited game")
