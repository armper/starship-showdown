
import pygame

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= 10  # Assuming BULLET_SPEED = 10

    def draw(self, surface):
        surface.blit(self.image, self.rect)
