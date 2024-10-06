import pygame
import random

class PowerUp:
    def __init__(self):
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 0), (10, 10), 10)  # Yellow circle
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.rect.width)  # SCREEN_WIDTH = 800
        self.rect.y = random.randint(-100, -40)
        self.speed = 3  # Reduced from 2

    def update(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)
