import pygame
from settings import PLAYER_SPEED

class Player:
    def __init__(self, x, y, character_name):
        self.character_name = character_name
        self.image = pygame.Surface((50, 80))
        self.image.fill(self.get_color_for_character())
        self.rect = self.image.get_rect(topleft=(x, y))

        self.is_punching = False
        self.punch_cooldown = 500  # milliseconds
        self.last_punch_time = 0

    def get_color_for_character(self):
        if self.character_name == "Graves":
            return (0, 128, 255)  # Blue
        elif self.character_name == "Red":
            return (255, 0, 0)  # Red
        elif self.character_name == "Vee":
            return (0, 255, 0)  # Green
        else:
            return (200, 200, 200)  # fallback grey

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        current_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE] and current_time - self.last_punch_time > self.punch_cooldown:
            self.is_punching = True
            self.last_punch_time = current_time
        else:
            self.is_punching = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
