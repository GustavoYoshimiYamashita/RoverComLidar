import funcoes_lidar
import mapa
import pygame

import serial

surface = mapa.iniciando_mapa(pygame)

ser = funcoes_lidar.iniciando_lidar()


contador = 0

while True:
    #mapa.atualiza_mapa_preto(surface)
    imagem_com_radianos, imagem_com_angulo = funcoes_lidar.coletando_dados_lidar(ser)
    imagem_cartesiana = mapa.transformando_polar_em_cartesiano(imagem_com_radianos, 300, 300)
    mapa.desenhando_mapa_2D(pygame, surface, imagem_cartesiana, 300, 300)
    pygame.display.update()
    pygame.display.flip()
    mapa.encerra_mapa(pygame)



