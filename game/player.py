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

        # Health system
        self.max_health = 3
        self.health = self.max_health
        self.alive = True

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
        if not self.alive:
            return

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

    def take_damage(self):
        if self.alive:
            self.health -= 1
            print("Player hit! Health left:", self.health)
            if self.health <= 0:
                self.alive = False
                print("Player died!")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # Health Bar
        health_bar_width = 50
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 10, health_bar_width, 5))
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, self.rect.y - 10, health_bar_width * health_ratio, 5))
