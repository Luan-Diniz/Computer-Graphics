import numpy as np

from src.interface.window import Window
from src.math.window_operations import WindowOperations


class DisplayFile:
    def __init__(self):
        self.lista_elementos_graficos = []

    def remover(self, i: int):
        self.lista_elementos_graficos.pop(i)

    def adicionar(self, elemento_grafico):
        self.lista_elementos_graficos.append(elemento_grafico)

    def getListaElementosGraficos(self):
        return self.lista_elementos_graficos

    def getNomesElementosGraficos(self):
        nomes = []
        for i in range(len(self.lista_elementos_graficos)):
            nomes.append(self.lista_elementos_graficos[i].get_nome())
        return nomes

    def getElementoGrafico(self, i):
        return self.lista_elementos_graficos[i]

    def calculaNormalizadas(self, window: Window):
        window.atualizaCoordenadaAposRotacao()
        # Centro da Window
        (Wxc, Wyc) = window.getCenter()

        matriz_tras_ao_centro = WindowOperations.cria_matriz_translacao(-Wxc, -Wyc)
        matriz_rotaciona = WindowOperations.cria_matriz_rotacao(
            -window.currentAngle()
        )  # Dentro da funcao vira radianos

        Sx = 1 / (0.5 * (window.Xwmax - window.Xwmin))
        Sy = 1 / (0.5 * (window.Ywmax - window.Ywmin))

        matriz_devolve_onde_estava = WindowOperations.cria_matriz_escalonamento(Sx, Sy)

        matriz_resultante = WindowOperations.junta_matrizes(
            matriz_tras_ao_centro, matriz_rotaciona, matriz_devolve_onde_estava
        )

        for elemento in self.lista_elementos_graficos:
            coordenadas = elemento.get_coordenadas()
            novas_coordenadas = []

            for x, y in coordenadas:
                pontos = np.array([[x, y, 1]])
                pontos_atualizados = np.dot(pontos, matriz_resultante)

                novas_coordenadas.append(pontos_atualizados.tolist()[0][0:2])

            elemento.set_coordenadas_normalizadas(
                novas_coordenadas
            )  # Atualiza as coordenadas normalizadas

        # window.atualizaCoordenadaAposRotacao()
