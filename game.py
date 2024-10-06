
import pygame
from spaceship import Spaceship
from bullet import Bullet
from alien import Alien
from utils import load_sounds

def game_over_screen(screen, score, game_over_sound):
    game_over_sound.play()
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height()))  # Assuming SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600
    screen.blit(score_text, (400 - score_text.get_width() // 2, 300 + text.get_height()))
    pygame.display.flip()
    pygame.time.wait(2000)

    # Wait for player to press a key to restart
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Assuming SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600
    pygame.display.set_caption("Spaceship Game")
    shoot_sound, explosion_sound, game_over_sound = load_sounds()

    while True:
        clock = pygame.time.Clock()
        running = True
        spaceship = Spaceship()
        bullets = []
        aliens = [Alien() for _ in range(5)]
        score = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Shoot a bullet
                        bullet = Bullet(spaceship.rect.centerx, spaceship.rect.top)
                        bullets.append(bullet)
                        shoot_sound.play()

            keys = pygame.key.get_pressed()
            dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5  # Assuming SPACESHIP_SPEED = 5
            dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
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
                    game_over_screen(screen, score, game_over_sound)
                # Check for collision with bullets
                for bullet in bullets[:]:
                    if alien.rect.colliderect(bullet.rect):
                        bullets.remove(bullet)
                        aliens.remove(alien)
                        aliens.append(Alien())
                        score += 1
                        explosion_sound.play()

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
            clock.tick(60)  # Assuming FPS = 60
