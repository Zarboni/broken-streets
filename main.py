import pygame
from game.player import Player
from game.level import Level
from game.character_select import CharacterSelect
from game.enemy import Enemy

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

# Game objects
player = Player(100, 500, selected_character)
enemy = Enemy(600, 500)
level = Level()

clock = pygame.time.Clock()

running = True
print("Entering game loop")

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event detected")
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)
    enemy.update(player.rect)

    # Punch Logic
    if player.is_punching and enemy.alive and player.rect.colliderect(enemy.rect):
        enemy.take_hit()

    level.draw(screen)
    player.draw(screen)
    enemy.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Exited game")
