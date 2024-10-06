
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SPACESHIP_SPEED = 5
BULLET_SPEED = 10
ALIEN_SPEED = 2

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spaceship Game")

# Load sounds
shoot_sound = pygame.mixer.Sound('shoot.wav')
explosion_sound = pygame.mixer.Sound('explosion.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

# Spaceship class
class Spaceship:
    def __init__(self):
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        # Draw a triangle
        pygame.draw.polygon(self.image, (255, 255, 255), [(0, 30), (25, 0), (50, 30)])
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Keep the spaceship on the screen
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= BULLET_SPEED

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Alien class
class Alien:
    def __init__(self):
        self.image = pygame.Surface((40, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += ALIEN_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True
    spaceship = Spaceship()
    bullets = []
    aliens = [Alien() for _ in range(5)]
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Shoot a bullet
                    bullet = Bullet(spaceship.rect.centerx, spaceship.rect.top)
                    bullets.append(bullet)

        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * SPACESHIP_SPEED
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * SPACESHIP_SPEED
        spaceship.move(dx, dy)

        # Update bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        # Update aliens
        for alien in aliens:
            alien.update()
            # Check for collision with spaceship
            if alien.rect.colliderect(spaceship.rect):
                running = False
            # Check for collision with bullets
            for bullet in bullets[:]:
                if alien.rect.colliderect(bullet.rect):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    aliens.append(Alien())
                    score += 1

        # Fill the screen with a black color
        screen.fill((0, 0, 0))
        spaceship.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for alien in aliens:
            alien.draw(screen)

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
