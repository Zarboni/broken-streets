import pygame
from game.player import Player
from game.level import Level
from game.character_select import CharacterSelect
from game.enemy import Enemy

def reset_game(screen):
    character_select = CharacterSelect(screen)
    selected_character = character_select.run()
    player = Player(100, 500, selected_character)
    enemy = Enemy(600, 500)
    level = Level()
    return player, enemy, level

pygame.init()
print("Pygame initialized")

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Broken Streets")
print("Window created")

# First time setup
character_select = CharacterSelect(screen)
selected_character = character_select.run()
print("Player selected:", selected_character)

player = Player(100, 500, selected_character)
enemy = Enemy(600, 500)
level = Level()

font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()
running = True
print("Entering game loop")

while running:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event detected")
            running = False

        # Handle Game Over input
        if not player.alive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("Restarting game...")
                    player, enemy, level = reset_game(screen)
                elif event.key == pygame.K_q:
                    print("Quitting game...")
                    running = False

    if player.alive:
        player.update(keys)
        enemy.update(player)

    # Combat
    if player.is_punching and enemy.alive and player.rect.colliderect(enemy.rect):
        enemy.take_hit()

    # Draw
    level.draw(screen)
    player.draw(screen)
    enemy.draw(screen)

    if not player.alive:
        text = font.render("GAME OVER – R to Restart, Q to Quit", True, (255, 255, 255))
        screen.blit(text, (100, 250))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Exited game")
