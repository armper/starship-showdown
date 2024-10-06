import pygame
import sys
import random
from spaceship import Spaceship
from bullet import Bullet
from alien import Alien
from powerup import PowerUp
from utils import load_sounds


def game_over_screen(screen, score, game_over_sound):
    game_over_sound.play()
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    # Assuming SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600
    screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height()))
    screen.blit(score_text, (400 - score_text.get_width() //
                2, 300 + text.get_height()))
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


def title_screen(screen):
    font = pygame.font.SysFont(None, 72)
    title_text = font.render("Starship Showdown", True, (255, 255, 255))
    instruction_text = font.render("Press SPACE to Start", True, (255, 255, 255))
    
    screen.fill((0, 0, 0))
    screen.blit(title_text, (400 - title_text.get_width() // 2, 250))
    screen.blit(instruction_text, (400 - instruction_text.get_width() // 2, 350))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Starship Showdown")
    shoot_sound, explosion_sound, game_over_sound, powerup_sound = load_sounds()

    title_screen(screen)

    while True:
        clock = pygame.time.Clock()
        running = True
        spaceship = Spaceship()
        bullets = []
        alien_speed_variation = 3  # Adjust this value as needed
        aliens = [Alien([], speed_variation=alien_speed_variation) for _ in range(3)]
        powerups = []
        score = 0
        level = 1
        powerup_active = False
        powerup_start_time = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if powerup_active:
                            angles = [-20, 0, 20]
                            for angle in angles:
                                bullet = Bullet(spaceship.rect.centerx, spaceship.rect.top, angle)
                                bullets.append(bullet)
                        else:
                            bullet = Bullet(spaceship.rect.centerx, spaceship.rect.top)
                            bullets.append(bullet)
                        shoot_sound.play()

            keys = pygame.key.get_pressed()
            dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
            dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
            spaceship.move(dx, dy)

            if random.randint(1, 1000) == 5:
                powerup = PowerUp()
                powerups.append(powerup)

            for bullet in bullets[:]:
                bullet.update()
                if (bullet.rect.bottom < 0 or bullet.rect.top > 600 or
                    bullet.rect.right < 0 or bullet.rect.left > 800):
                    bullets.remove(bullet)

            for alien in aliens[:]:
                alien.update()

                if alien.rect.colliderect(spaceship.rect):
                    running = False
                    game_over_screen(screen, score, game_over_sound)
                    continue

                for bullet in bullets[:]:
                    if alien.rect.colliderect(bullet.rect):
                        bullets.remove(bullet)
                        aliens.remove(alien)
                        # Pass speed_variation when creating a new alien
                        aliens.append(Alien(aliens, speed_variation=alien_speed_variation))
                        score += 1
                        explosion_sound.play()
                        break

                else:
                    if alien.rect.top > 600:
                        score -= 1
                        if score <= 0:
                            running = False
                            game_over_screen(screen, score, game_over_sound)
                        aliens.remove(alien)
                        # Pass speed_variation when creating a new alien
                        aliens.append(Alien(aliens, speed_variation=alien_speed_variation))

            for powerup in powerups[:]:
                powerup.update()
                if powerup.rect.colliderect(spaceship.rect):
                    powerups.remove(powerup)
                    powerup_active = True
                    powerup_start_time = pygame.time.get_ticks()
                    powerup_sound.play()
                elif powerup.rect.top > 600:
                    powerups.remove(powerup)

            if powerup_active and pygame.time.get_ticks() - powerup_start_time > 10000:
                powerup_active = False

            if score >= level * 15:
                level += 1
                # Pass speed_variation when adding new aliens for the new level
                aliens.extend(
                    Alien(aliens, speed_variation=alien_speed_variation)
                    for _ in range(1 + level // 2)
                )

            screen.fill((0, 0, 0))
            spaceship.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            for alien in aliens:
                alien.draw(screen)
            for powerup in powerups:
                powerup.draw(screen)

            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            level_text = font.render(f"Level: {level}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            screen.blit(level_text, (10, 50))

            pygame.display.flip()
            clock.tick(60)
