import pygame

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 80))
        self.image.fill((128, 0, 128))  # Purple
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        self.health = 3
        self.alive = True

        # Attack system
        self.attack_cooldown = 1000  # milliseconds
        self.last_attack_time = 0

    def update(self, player):
        if not self.alive:
            return

        # Movement
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        # Attack logic
        current_time = pygame.time.get_ticks()
        if self.rect.colliderect(player.rect) and current_time - self.last_attack_time > self.attack_cooldown:
            self.last_attack_time = current_time
            player.take_damage()

    def take_hit(self):
        self.health -= 1
        print("Enemy hit! Health left:", self.health)
        if self.health <= 0:
            self.alive = False
            print("Enemy defeated!")

    def draw(self, screen):
        if self.alive:
            # Draw health bar
            health_bar_width = 50
            health_ratio = self.health / 3
            pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 10, health_bar_width, 5))
            pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, self.rect.y - 10, health_bar_width * health_ratio, 5))

        screen.blit(self.image, self.rect)
