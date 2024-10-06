
import pygame

# Spaceship class
class Spaceship:
    def __init__(self):
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        # Draw a triangle
        pygame.draw.polygon(self.image, (255, 255, 255), [(0, 30), (25, 0), (50, 30)])
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)  # Assuming SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Keep the spaceship on the screen
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
