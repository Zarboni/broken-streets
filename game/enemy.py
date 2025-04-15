import pygame

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 80))
        self.image.fill((128, 0, 128))  # Purple
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.health = 3
        self.alive = True

    def update(self, player_rect):
        if not self.alive:
            return

        if self.rect.x < player_rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player_rect.x:
            self.rect.x -= self.speed

    def take_hit(self):
        self.health -= 1
        print("Enemy hit! Health left:", self.health)
        if self.health <= 0:
            self.alive = False

    def draw(self, screen):
        if self.alive:
            # Draw health bar
            health_bar_width = 50
            health_ratio = self.health / 3
            pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 10, health_bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, self.rect.y - 10, health_bar_width * health_ratio, 5))

        screen.blit(self.image, self.rect)
