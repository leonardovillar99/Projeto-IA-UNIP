#Importando as dependências do projeto
import pygame
from pygame.locals import *
from sys import exit

#Iniciando a biblioteca pygame
pygame.init()

#Largura e Altura da Tela
width = 800
height = 800

# Variáveis que controlam o movimento do personagem no mapa
x = 0
y = 0

# Setando as variáveis de altura e largura no método display.set_mode
screen = pygame.display.set_mode((width, height))

#Alterando o Título da Tela
pygame.display.set_caption('IA - Dragon Ball Z')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #pygame.draw.rect(screen, (255, 255, 0), (0,400,100,400))
        scale = pygame.transform.scale
        image = scale(pygame.image.load("src/images/map.png"),(400,400))
        pygame.display.update()