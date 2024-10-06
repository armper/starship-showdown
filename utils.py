import pygame

def load_sounds():
    try:
        pygame.mixer.init()  # Initialize the mixer
        shoot_sound = pygame.mixer.Sound('shoot.wav')
        explosion_sound = pygame.mixer.Sound('explosion.wav')
        game_over_sound = pygame.mixer.Sound('game_over.wav')
        powerup_sound = pygame.mixer.Sound('powerup.wav')  # Load the power-up sound
    except pygame.error:
        class DummySound:
            def play(self):
                pass
        shoot_sound = explosion_sound = game_over_sound = powerup_sound = DummySound()
    return shoot_sound, explosion_sound, game_over_sound, powerup_sound
