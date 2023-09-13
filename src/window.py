import numpy as np
from math import cos, sin, tan
from config import Config
from window_auxiliary import WindowAuxiliary


class Window:
    def __init__(self):
        # Coordenadas do mundo real
        self.Xwmin = Config.window_Xwmin()
        self.Xwmax = Config.window_Xwmax()
        self.Ywmin = Config.window_Ywmin()
        self.Ywmax = Config.window_Ywmax()
        self.scale = Config.scale()

        self.view_up_vector = np.array([0,1])

        self.Xwminnormalizado = -1
        self.Xwmaxnormalizado = 1
        self.Ywminnormalizado = -1
        self.Ywmaxnormalizado = 1

        self.coordenadas = [(self.Xwmin, self.Ywmin),(self.Xwmax, self.Ywmin),(self.Xwmin, self.Ywmax),(self.Xwmax, self.Ywmax)]

        self.angle = 0  # Em graus
        self.angle_variation = 0 #Quando a window rotacionar, isso armazenara o angulo até que seus pontos sejam atualizados. (Um buffer)

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
        contx, conty = 0, 0

        for x, y in self.coordenadas:
            contx+= x
            conty+= y

        return (contx / 4, conty / 4)

    def rotacionaAntiHorario(self):
        self.angle += Config.window_rotation_angle()
        self.angle_variation += Config.window_rotation_angle()

        self.atualizaViewUpVector()

    def rotatacionaHorario(self):
        self.angle -= Config.window_rotation_angle()
        self.angle_variation -= Config.window_rotation_angle()

        self.atualizaViewUpVector()

    def atualizaCoordenadaAposRotacao(self):
        if self.angle_variation != 0: #Ou seja, houve uma rotacao
            dx,dy = self.getCenter()
            matriz_translacao1 = np.array([[1, 0, 0], [0, 1, 0], [-dx, -dy, 1]])
            matriz_rotacao = np.array(
                [
                    [cos(self.angle_variation), -sin(self.angle_variation), 0],
                    [sin(self.angle_variation), cos(self.angle_variation), 0],
                    [0, 0, 1],
                ]
            )
            matriz_translacao2 = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])
            matriz_resultante = np.dot(matriz_translacao1, np.dot(matriz_rotacao, matriz_translacao2))




            novos_pontos_lista = []
            for x,y in self.coordenadas:
                pontos = np.array([[x,y,1]])
                novos_pontos = np.dot(pontos, matriz_resultante)

                novos_pontos_lista.append(   novos_pontos.tolist()[0][0:2])
                #print(novos_pontos.tolist()[0][0:2])

            self.angle_variation = 0 #Coordenadas foram atualizadas, logo reseta o buffer

    def atualizaViewUpVector(self):
        if self.angle == 90:
            self.view_up_vector = np.array([-1,0])

        elif self.angle == 270:
            self.view_up_vector = np.array([1,0])

        else:
            #Recalculando valor do vetor unitário.
            (n,m) = WindowAuxiliary.float_to_fraction(tan(self.angle))
            modulo_vetor = (n**2 + m**2) ** 0.5
            n = n/modulo_vetor
            m = m/modulo_vetor

            self.view_up_vector = np.array([n,m])


    def currentAngle(self):
        return self.angle

    def setAngle(self, angulo):
        self.angle = angulo
