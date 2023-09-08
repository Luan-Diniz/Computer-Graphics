import numpy as np

from config import Config


class Window:
    def __init__(self):
        # Coordenadas do mundo real
        self.Xwmin = Config.window_Xwmin()
        self.Xwmax = Config.window_Xwmax()
        self.Ywmin = Config.window_Ywmin()
        self.Ywmax = Config.window_Ywmax()
        self.scale = Config.scale()

        self.Xwminnormalizado = -1
        self.Xwmaxnormalizado = 1
        self.Ywminnormalizado = -1
        self.Ywmaxnormalizado = 1

        self.angle = 0  # Em graus

    def moveuDireita(self):
        deltax = self.Xwmax - self.Xwmin

        self.Xwmin += (deltax) * self.scale
        self.Xwmax += (deltax) * self.scale

    def moveuEsquerda(self):
        deltax = self.Xwmax - self.Xwmin

        self.Xwmin -= (deltax) * self.scale
        self.Xwmax -= (deltax) * self.scale

    def moveuCima(self):
        deltay = self.Ywmax - self.Ywmin

        self.Ywmin += (deltay) * self.scale
        self.Ywmax += (deltay) * self.scale

    def moveuBaixo(self):
        deltay = self.Ywmax - self.Ywmin

        self.Ywmin -= (deltay) * self.scale
        self.Ywmax -= (deltay) * self.scale

    def ZoomIn(self):
        # A Window fica menor, logo as imagens que ela ve sao "maiores"
        deltax = self.Xwmax - self.Xwmin
        deltay = self.Ywmax - self.Ywmin

        self.Xwmin += (deltax) * self.scale
        self.Xwmax -= (deltax) * self.scale
        self.Ywmin += (deltay) * self.scale
        self.Ywmax -= (deltay) * self.scale

    def ZoomOut(self):
        # A Window fica maior, logo as imagens que ela ve sao "menores"
        deltax = self.Xwmax - self.Xwmin
        deltay = self.Ywmax - self.Ywmin

        self.Xwmin -= (deltax) * self.scale
        self.Xwmax += (deltax) * self.scale
        self.Ywmin -= (deltay) * self.scale
        self.Ywmax += (deltay) * self.scale

    def getCenter(self) -> tuple:
        return ((self.Xwmax + self.Xwmin) / 2, (self.Ywmax + self.Ywmin) / 2)

    def rotacionaAntiHorario(self):
        self.angle += Config.window_rotation_angle()

    def rotatacionaHorario(self):
        self.angle -= Config.window_rotation_angle()

    def currentAngle(self):
        return self.angle

    def setAngle(self, angulo):
        self.angle = angulo
