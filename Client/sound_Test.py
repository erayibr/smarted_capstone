import pygame
pygame.mixer.init()
pygame.mixer.music.load("applause-1.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue