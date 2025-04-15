import pygame
from settings import PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 80))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)
