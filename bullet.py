import pygame
import math

# Bullet class
class Bullet:
    def __init__(self, x, y, angle=0):
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = angle
        self.speed = 10  # Bullet speed

        radians = math.radians(self.angle)
        self.vx = self.speed * math.sin(radians)
        self.vy = -self.speed * math.cos(radians)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self, surface):
        surface.blit(self.image, self.rect)
