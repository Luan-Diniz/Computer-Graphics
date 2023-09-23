import numpy as np

from src.interface.config import Config


class Clipping:
    @staticmethod
    def point_clippig(X: int, Y: int) -> bool:
        Xwmin = Config.window_Xwmin()
        Xwmax = Config.window_Xwmax()
        Ywmin = Config.window_Ywmin()
        Ywmax = Config.window_Ywmax()
        if (Xwmin <= X <= Xwmax) and (Ywmin <= Y <= Ywmax):
            return True
        return True  # Remover
        return False

    def cohen_sutherland(pontos):
        return pontos

    def liang_barsky():
        pass

    def sutherland_hodgeman():
        pass


"""
# GEEKS FOR GEEKS
# Programa em Python para implementar o algoritmo Cohen-Sutherland
# para recorte de linha.

# Definindo códigos de região
DENTRO = 0    # 0000
ESQUERDA = 1  # 0001
DIREITA = 2   # 0010
ABAIXO = 4    # 0100
ACIMA = 8     # 1000

# Definindo x_max, y_max e x_min, y_min para o retângulo
# Como os pontos diagonais são suficientes para definir um retângulo
x_max = 10.0
y_max = 8.0
x_min = 4.0
y_min = 4.0

# Função para calcular o código de região para um ponto (x, y)
def calcularCodigo(x, y):
    codigo = DENTRO
    if x < x_min:  # à esquerda do retângulo
        codigo |= ESQUERDA
    elif x > x_max:  # à direita do retângulo
        codigo |= DIREITA
    if y < y_min:  # abaixo do retângulo
        codigo |= ABAIXO
    elif y > y_max:  # acima do retângulo
        codigo |= ACIMA
    return codigo

# Implementando o algoritmo Cohen-Sutherland
# Recortando uma linha de P1 = (x1, y1) para P2 = (x2, y2)
def cohenSutherlandClip(x1, y1, x2, y2):

    # Calcular códigos de região para P1, P2
    codigo1 = calcularCodigo(x1, y1)
    codigo2 = calcularCodigo(x2, y2)
    aceitar = False

    while True:

        # Se ambos os pontos finais estão dentro do retângulo
        if codigo1 == 0 and codigo2 == 0:
            aceitar = True
            break

        # Se ambos os pontos finais estão fora do retângulo
        elif (codigo1 & codigo2) != 0:
            break

        # Algum segmento está dentro do retângulo
        else:

            # A linha precisa ser recortada
            # Pelo menos um dos pontos está fora,
            # selecione-o
            x = 1.0
            y = 1.0
            if codigo1 != 0:
                codigo_fora = codigo1
            else:
                codigo_fora = codigo2

            # Encontrar ponto de interseção
            # usando as fórmulas y = y1 + inclinação * (x - x1),
            # x = x1 + (1 / inclinação) * (y - y1)
            if codigo_fora & ACIMA:
                # O ponto está acima do retângulo de recorte
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif codigo_fora & ABAIXO:
                # O ponto está abaixo do retângulo de recorte
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif codigo_fora & DIREITA:
                # O ponto está à direita do retângulo de recorte
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif codigo_fora & ESQUERDA:
                # O ponto está à esquerda do retângulo de recorte
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            # Agora o ponto de interseção (x, y) é encontrado
            # Substituímos o ponto fora do retângulo de recorte
            # pelo ponto de interseção
            if codigo_fora == codigo1:
                x1 = x
                y1 = y
                codigo1 = calcularCodigo(x1, y1)
            else:
                x2 = x
                y2 = y
                codigo2 = calcularCodigo(x2, y2)

    if aceitar:
        print("Linha aceita de %.2f, %.2f a %.2f, %.2f" % (x1, y1, x2, y2))

        # Aqui o usuário pode adicionar código para exibir o retângulo
        # juntamente com as linhas aceitas (parte delas)

    else:
        print("Linha rejeitada")

# Script de driver

# Primeiro segmento de linha
# P11 = (5, 5), P12 = (7, 7)
cohenSutherlandClip(5, 5, 7, 7)

# Segundo segmento de linha
# P21 = (7, 9), P22 = (11, 4)
cohenSutherlandClip(7, 9, 11, 4)

# Terceiro segmento de linha
# P31 = (1, 5), P32 = (4, 1)
cohenSutherlandClip(1, 5, 4, 1)
"""
