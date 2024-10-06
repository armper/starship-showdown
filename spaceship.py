import pygame

# Spaceship class
class Spaceship:
    def __init__(self):
        self.frames = [pygame.image.load(f"player_frame_{i}.png").convert_alpha() for i in range(1)]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)  # Assuming SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600
        self.animation_speed = 0.1  # Adjust this value to change the speed of the animation
        self.last_update = pygame.time.get_ticks()
        
        # New attributes for speed and acceleration
        self.base_speed = 3.35  # Reduced from 5
        self.acceleration = 0.21  # Reduced from 0.31415
        self.max_speed = 6.7  # Reduced from 10
        self.current_speed_x = 0
        self.current_speed_y = 0

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 1000 * self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    def move(self, dx, dy):
        # Accelerate the spaceship
        if dx != 0:
            self.current_speed_x += self.acceleration * dx
            self.current_speed_x = max(-self.max_speed, min(self.current_speed_x, self.max_speed))
        else:
            self.current_speed_x = 0  # Reset speed when no key is pressed

        if dy != 0:
            self.current_speed_y += self.acceleration * dy
            self.current_speed_y = max(-self.max_speed, min(self.current_speed_y, self.max_speed))
        else:
            self.current_speed_y = 0  # Reset speed when no key is pressed

        # Move the spaceship
        self.rect.x += self.current_speed_x
        self.rect.y += self.current_speed_y

        # Ensure the spaceship stays within the screen bounds
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
