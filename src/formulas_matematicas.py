from math import cos, radians, sin

import numpy as np

from viewport import ViewPort
from window import Window


class FormulasMatematicas:
    @staticmethod
    def calcular_x_viewport(Xw: float, window: Window) -> float:
        # Xw é uma coordenada X no sistema cartesiano da Window
        viewport_variance = ViewPort.viewportXmax() - ViewPort.viewportXmin()
        return ((Xw - window.Xwminnormalizado) / (window.Xwmaxnormalizado - window.Xwminnormalizado)) * viewport_variance

    @staticmethod
    def calcular_y_viewport(Yw: float, window: Window) -> float:
        # Yw é uma coordenada Y no sistema cartesiano da Window
        viewport_variance = ViewPort.viewportYmax() - ViewPort.viewportYmin()
        return (
            1 - ((Yw - window.Ywminnormalizado) / (window.Ywmaxnormalizado - window.Ywminnormalizado))
        ) * viewport_variance

    @staticmethod
    def transformada_viewport(Xw: float, Yw: float, window: Window) -> tuple:
        X_viewport = FormulasMatematicas.calcular_x_viewport(Xw, window)
        Y_viewport = FormulasMatematicas.calcular_y_viewport(Yw, window)

        return (X_viewport, Y_viewport)

    @staticmethod
    def junta_matrizes(*args):
        primeira = True
        matriz_final = []
        for i in args:
            if primeira == True:
                matriz_final = i
                primeira = False
            else:
                matriz_final = np.dot(matriz_final, i)  # Multiplica as matrizes
        return matriz_final

    @staticmethod
    def cria_matriz_translacao(desvio_x, desvio_y):
        return np.array([[1, 0, 0], [0, 1, 0], [desvio_x, desvio_y, 1]])

    @staticmethod
    def cria_matriz_rotacao(angulo):
        angulo = radians(-angulo)

        return np.array(
            [
                [cos(angulo), -sin(angulo), 0],
                [sin(angulo), cos(angulo), 0],
                [0, 0, 1],
            ]
        )

    @staticmethod
    def cria_matriz_escalonamento(Sx, Sy):
        return np.array(
            [[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]]
        )
