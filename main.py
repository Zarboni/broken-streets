import pygame
from game.player import Player
from game.level import Level
from game.character_select import CharacterSelect

pygame.init()
print("Pygame initialized")

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Broken Streets")
print("Window created")

# Character selection happens here
character_select = CharacterSelect(screen)
selected_character = character_select.run()


print("Player selected:", selected_character)

clock = pygame.time.Clock()

player = Player(100, 500)  # later we’ll pass `selected_character`
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
