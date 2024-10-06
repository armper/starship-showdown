import pygame
import random

# Alien class
class Alien:
    def __init__(self):
        self.image = pygame.Surface((40, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.rect.width)  # Assuming SCREEN_WIDTH = 800
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += 2  # Assuming ALIEN_SPEED = 2

    def draw(self, surface):
        surface.blit(self.image, self.rect)
