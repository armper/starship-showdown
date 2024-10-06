
import pygame

def load_sounds():
    shoot_sound = pygame.mixer.Sound('shoot.wav')
    explosion_sound = pygame.mixer.Sound('explosion.wav')
    game_over_sound = pygame.mixer.Sound('game_over.wav')
    return shoot_sound, explosion_sound, game_over_sound
