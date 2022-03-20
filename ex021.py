import pygame
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
x = input('digite algo para encerrar ...')

#
# OU É POSSÍVEL USAR
# while(pygame.mixer.music.get_busy()): pass
#       :)
#