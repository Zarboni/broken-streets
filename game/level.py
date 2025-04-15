import pygame

class Level:
    def __init__(self):
        self.background = pygame.Surface((800, 600))
        self.background.fill((50, 50, 50))  # Dark grey

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
