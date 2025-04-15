import pygame

class CharacterSelect:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 40)
        self.characters = ["Graves", "Red", "Vee"]
        self.selected_index = 0

    def run(self):
        selecting = True

        while selecting:
            self.screen.fill((0, 0, 0))  # Black background

            title = self.font.render("Select Your Fighter", True, (255, 255, 255))
            self.screen.blit(title, (250, 100))

            for idx, name in enumerate(self.characters):
                color = (255, 0, 0) if idx == self.selected_index else (255, 255, 255)
                text = self.font.render(name, True, color)
                self.screen.blit(text, (350, 200 + idx * 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.characters)
                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.characters)
                    if event.key == pygame.K_RETURN:
                        selecting = False

        return self.characters[self.selected_index]
