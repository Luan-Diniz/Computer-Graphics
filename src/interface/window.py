from math import cos, radians, sin

import numpy as np
from src.interface.config import Config
from src.math.window_operations import WindowOperations


class Window:
    def __init__(self):
        # Coordenadas do mundo real
        self.Xwmin = Config.window_Xwmin()
        self.Xwmax = Config.window_Xwmax()
        self.Ywmin = Config.window_Ywmin()
        self.Ywmax = Config.window_Ywmax()
        self.scale = Config.scale()

        self.view_up_vector = np.array([0, 1])
        self.vpn = np.array([0, 0, 1])

        self.Xwminnormalizado = -1
        self.Xwmaxnormalizado = 1
        self.Ywminnormalizado = -1
        self.Ywmaxnormalizado = 1

        self.coordenadas = [
            (self.Xwmin, self.Ywmin, 0),
            (self.Xwmax, self.Ywmin, 0),
            (self.Xwmin, self.Ywmax, 0),
            (self.Xwmax, self.Ywmax, 0),
        ]

        self.angle = 0  # Em graus
        self.angle_variation = 0  # Quando a window rotacionar, isso armazenara o angulo até que seus pontos sejam atualizados. (Um buffer)

    def moveuDireita(self):
        distance = (self.Xwmax - self.Xwmin) * self.scale

        n = self.view_up_vector[0]
        m = self.view_up_vector[1]
        vetor = WindowOperations.rotaciona_pontos([(n, m)], radians(-90))

        vetor = np.array([vetor[0][0], vetor[0][1]])

        distance = distance * vetor

        matriz_translacao = WindowOperations.cria_matriz_translacao(
            distance[0], distance[1]
        )

        novas_coordenadas = []
        for x, y, z in self.coordenadas:
            novos_pontos = np.dot(np.array([x, y, 1]), matriz_translacao)
            novas_coordenadas.append((novos_pontos[0], novos_pontos[1], z))

        self.coordenadas = novas_coordenadas

        """
        self.Xwmin += (deltax) * self.scale
        self.Xwmax += (deltax) * self.scale
        """

    def moveuEsquerda(self):
        distance = (self.Xwmax - self.Xwmin) * self.scale

        n = self.view_up_vector[0]
        m = self.view_up_vector[1]
        vetor = WindowOperations.rotaciona_pontos([(n, m)], radians(90))

        vetor = np.array([vetor[0][0], vetor[0][1]])

        distance = distance * vetor

        matriz_translacao = WindowOperations.cria_matriz_translacao(
            distance[0], distance[1]
        )

        novas_coordenadas = []
        for x, y, z in self.coordenadas:
            novos_pontos = np.dot(np.array([x, y, 1]), matriz_translacao)
            novas_coordenadas.append((novos_pontos[0], novos_pontos[1], z))

        self.coordenadas = novas_coordenadas

        """
        deltax = self.Xwmax - self.Xwmin
        self.Xwmin -= (deltax) * self.scale
        self.Xwmax -= (deltax) * self.scale
        """

    def moveuCima(self):
        distance = (self.Xwmax - self.Xwmin) * self.scale
        distance = distance * self.view_up_vector * -1

        matriz_translacao = WindowOperations.cria_matriz_translacao(
            distance[0], distance[1]
        )

        novas_coordenadas = []
        for x, y, z in self.coordenadas:
            novos_pontos = np.dot(np.array([x, y, 1]), matriz_translacao)
            novas_coordenadas.append((novos_pontos[0], novos_pontos[1], z))

        self.coordenadas = novas_coordenadas

        """
        deltay = self.Ywmax - self.Ywmin

        
        self.Ywmin += (deltay) * self.scale
        self.Ywmax += (deltay) * self.scale
        """

    def moveuBaixo(self):
        distance = (self.Xwmax - self.Xwmin) * self.scale
        distance = distance * self.view_up_vector

        matriz_translacao = WindowOperations.cria_matriz_translacao(
            distance[0], distance[1]
        )

        novas_coordenadas = []
        for x, y, z in self.coordenadas:
            novos_pontos = np.dot(np.array([x, y, 1]), matriz_translacao)
            novas_coordenadas.append((novos_pontos[0], novos_pontos[1], z))

        self.coordenadas = novas_coordenadas

        """
        deltay = self.Ywmax - self.Ywmin

        self.Ywmin -= (deltay) * self.scale
        self.Ywmax -= (deltay) * self.scale
        """

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
        contx, conty, contz = 0, 0, 0

        for x, y, z in self.coordenadas:
            contx += x
            conty += y
            contz += z

        return (contx / 4, conty / 4, contz / 4)

    def rotacionaAntiHorario(self):
        self.angle += Config.window_rotation_angle()
        self.angle_variation += Config.window_rotation_angle()

        self.atualizaViewUpVector()

    def rotatacionaHorario(self):
        self.angle -= Config.window_rotation_angle()
        self.angle_variation -= Config.window_rotation_angle()

        self.atualizaViewUpVector()

    def atualizaCoordenadaAposRotacao(self):
        if self.angle_variation != 0:  # Ou seja, houve uma rotacao
            dx, dy, dz = self.getCenter()
            matriz_translacao1 = np.array([[1, 0, 0], [0, 1, 0], [-dx, -dy, 1]])
            matriz_rotacao = np.array(
                [
                    [cos(self.angle_variation), -sin(self.angle_variation), 0],
                    [sin(self.angle_variation), cos(self.angle_variation), 0],
                    [0, 0, 1],
                ]
            )
            matriz_translacao2 = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])
            matriz_resultante = np.dot(
                matriz_translacao1, np.dot(matriz_rotacao, matriz_translacao2)
            )

            novos_pontos_lista = []
            for x, y, z in self.coordenadas:
                pontos = np.array([[x, y, 1]])
                novos_pontos = np.dot(pontos, matriz_resultante)
                novos_pontos = novos_pontos.tolist()[0][0:2]
                novos_pontos.append(z)
                novos_pontos_lista.append(novos_pontos)

            self.coordenadas = novos_pontos_lista
            self.angle_variation = (
                0  # Coordenadas foram atualizadas, logo reseta o buffer
            )

    def atualizaViewUpVector(self):
        n = self.view_up_vector[0]
        m = self.view_up_vector[1]

        pontos = WindowOperations.rotaciona_pontos(
            [(n, m)], radians(-self.angle_variation)
        )
        n = pontos[0][0]
        m = pontos[0][1]
        self.view_up_vector = np.array([n, m])

    def currentAngle(self):
        return self.angle

    def setAngle(self, angulo):
        self.angle = angulo

    def projecao(self, angulo):
        pass
        WindowOperations.rotacao3DY(angulo)

    def rotacionaAntiHorario3D(self):
        angulo = radians(45)
        novas_coordenadas = []
        Cx, Cy, Cz = self.getCenter()
        for x, y, z in self.coordenadas:
            matriz_pontos = np.array([[x, y, z, 1]])

            matriz_translacao1 = np.array(
                [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-Cx, -Cy, -Cz, 1]]
            )

            matriz_rotacao = np.array(
                [
                    [cos(angulo), 0, -sin(angulo), 0],
                    [0, 1, 0, 0],
                    [sin(angulo), 0, cos(angulo), 0],
                    [0, 0, 0, 1],
                ]
            )
            matriz_translacao2 = np.array(
                [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [Cx, Cy, Cz, 1]]
            )

            matriz_operation = WindowOperations.junta_matrizes(
                matriz_translacao1,
                matriz_rotacao,
                matriz_translacao2,
            )
            matriz_novos_pontos = np.dot(matriz_pontos, matriz_operation)

            novas_coordenadas.append(
                (
                    matriz_novos_pontos[0][0],
                    matriz_novos_pontos[0][1],
                    matriz_novos_pontos[0][2],
                )
            )

        self.coordenadas = novas_coordenadas
        self.angle += Config.window_rotation_angle()
        self.angle_variation += Config.window_rotation_angle()
        self.atualizaViewUpVector()

    def rotatacionaHorario3D(self):
        angulo = radians(-45)
        novas_coordenadas = []
        Cx, Cy, Cz = self.getCenter()
        for x, y, z in self.coordenadas:
            matriz_pontos = np.array([[x, y, z, 1]])

            matriz_translacao1 = np.array(
                [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-Cx, -Cy, -Cz, 1]]
            )

            matriz_rotacao = np.array(
                [
                    [cos(angulo), 0, -sin(angulo), 0],
                    [0, 1, 0, 0],
                    [sin(angulo), 0, cos(angulo), 0],
                    [0, 0, 0, 1],
                ]
            )
            matriz_translacao2 = np.array(
                [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [Cx, Cy, Cz, 1]]
            )

            matriz_operation = WindowOperations.junta_matrizes(
                matriz_translacao1,
                matriz_rotacao,
                matriz_translacao2,
            )
            matriz_novos_pontos = np.dot(matriz_pontos, matriz_operation)

            novas_coordenadas.append(
                (
                    matriz_novos_pontos[0][0],
                    matriz_novos_pontos[0][1],
                    matriz_novos_pontos[0][2],
                )
            )

        self.coordenadas = novas_coordenadas
        self.angle += Config.window_rotation_angle()
        self.angle_variation += Config.window_rotation_angle()
        self.atualizaViewUpVector()
