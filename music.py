import pygame

def play_music(music):
    # Load the music file
    music_file = music

    pygame.init()

    # Load pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)

    # Loop over the music file
    pygame.mixer.music.play(-1)
