# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# 1º passo: Importar a biblioteca
import pygame
# 2º passo: iniciar o pygame
pygame.init()
# 3º passo: arquivo que carrega a música
pygame.mixer.music.load('ex021.mp3')
# 4º passo: arquivo ira tocar
pygame.mixer.music.play()
# 5º passo: esperar a música terminar
pygame.event.wait()
