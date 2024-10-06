import pygame
import random

# Alien class
class Alien:
    def __init__(self, existing_aliens):
        self.frames = [pygame.image.load(f"alien_frame_{i}.png").convert_alpha() for i in range(1)]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.get_valid_position(existing_aliens)
        self.animation_speed = 0.1  # Adjust this value to change the speed of the animation
        self.last_update = pygame.time.get_ticks()

    def get_valid_position(self, existing_aliens):
        min_distance = 30  # Adjust this value to change the minimum spacing
        while True:
            x = random.randint(0, 800 - self.rect.width)
            y = random.randint(-100, -40)
            if all(self.distance((x, y), (alien.rect.x, alien.rect.y)) >= min_distance for alien in existing_aliens):
                return x, y

    def distance(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 1000 * self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
        self.rect.y += 2  # Assuming ALIEN_SPEED = 2

    def draw(self, surface):
        surface.blit(self.image, self.rect)
