from math import cos, floor, radians, sin

import numpy as np


class WindowOperations:
    @staticmethod
    def float_to_fraction(x, error=0.000001):
        n = int(floor(x))
        x -= n
        if x < error:
            return (n, 1)
        elif 1 - error < x:
            return (n + 1, 1)

        # The lower fraction is 0/1
        lower_n = 0
        lower_d = 1
        # The upper fraction is 1/1
        upper_n = 1
        upper_d = 1
        while True:
            # The middle fraction is (lower_n + upper_n) / (lower_d + upper_d)
            middle_n = lower_n + upper_n
            middle_d = lower_d + upper_d
            # If x + error < middle
            if middle_d * (x + error) < middle_n:
                # middle is our new upper
                upper_n = middle_n
                upper_d = middle_d
            # Else If middle < x - error
            elif middle_n < (x - error) * middle_d:
                # middle is our new lower
                lower_n = middle_n
                lower_d = middle_d
            # Else middle is our best fraction
            else:
                return (n * middle_d + middle_n, middle_d)

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
        return np.array([[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]])

    @staticmethod
    def rotaciona_pontos(lista_pontos, angulo):
        novos_pontos = []
        angulo = angulo

        dx, dy = 0, 0

        matriz_translacao1 = np.array([[1, 0, 0], [0, 1, 0], [-dx, -dy, 1]])

        matriz_rotacao = np.array(
            [
                [cos(angulo), -sin(angulo), 0],
                [sin(angulo), cos(angulo), 0],
                [0, 0, 1],
            ]
        )
        matriz_translacao2 = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])

        matriz_resultante = np.dot(
            matriz_translacao1, np.dot(matriz_rotacao, matriz_translacao2)
        )

        for i, j in lista_pontos:
            pontos = np.array([[i, j, 1]])
            pontos_atualizados = np.dot(pontos, matriz_resultante)

            novos_pontos.append((pontos_atualizados[0][0], pontos_atualizados[0][1]))

        return novos_pontos

    # ----------------------------3D----------------------------------
    @staticmethod
    def translacao3D(elemento_grafico, coordinates):
        coordenadas_atualizadas = []
        (desvio_x, desvio_y, desvio_z) = coordinates

        matriz_translacao = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [desvio_x, desvio_y, desvio_z, 1],
            ]
        )

        for i, j, k in elemento_grafico.get_coordenadas():
            pontos = np.array([[i, j, k, 1]])
            pontos_atualizados = np.dot(pontos, matriz_translacao)

            coordenadas_atualizadas.append(
                (
                    pontos_atualizados[0][0],
                    pontos_atualizados[0][1],
                    pontos_atualizados[0][2],
                )
            )

        # Atualiza as coordenadas
        elemento_grafico.set_coordenadas(coordenadas_atualizadas)

    @staticmethod
    def escalonamento3D(elemento_grafico, coef_escalonamento):
        coordenadas_atualizadas = []
        (cx, cy, cz) = elemento_grafico.get_centro3D()

        if coef_escalonamento == 0:
            return -1

        matriz_traz_ao_centro = np.array(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-cx, -cy, -cz, 1]]
        )
        matriz_escalona = np.array(
            [
                [coef_escalonamento, 0, 0, 0],
                [0, coef_escalonamento, 0, 0],
                [0, 0, coef_escalonamento, 0, 0],
                [0, 0, 0, 1],
            ]
        )
        matriz_devolve_ao_local_original = np.array(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [cx, cy, cz, 1]]
        )

        matriz_resultante = WindowOperations.junta_matrizes(
            matriz_traz_ao_centro,
            matriz_escalona,
            matriz_devolve_ao_local_original,
        )

        for i, j, k in elemento_grafico.get_coordenadas():
            pontos = np.array([[i, j, k, 1]])
            pontos_atualizados = np.dot(pontos, matriz_resultante)

            coordenadas_atualizadas.append(
                (
                    pontos_atualizados[0][0],
                    pontos_atualizados[0][1],
                    pontos_atualizados[0][2],
                )
            )

        # Atualiza as coordenadas
        elemento_grafico.set_coordenadas(coordenadas_atualizadas)

    @staticmethod
    def rotacao3DX(elemento_grafico, angulo):
        Cx, Cy, Cz = elemento_grafico.get_centro3D()
        WindowOperations.translacao(elemento_grafico, (-Cx, -Cy, -Cz))

        matriz_rotacao = np.array(
            [
                [1, 0, 0, 0],
                [0, cos(angulo), sin(angulo), 0],
                [0, -sin(angulo), cos(angulo), 0],
                [0, 0, 0, 1],
            ]
        )

        novas_coordenadas = []
        for i, j, k in elemento_grafico.get_coordenadas():
            pontos = np.array([[i, j, k, 1]])
            pontos_atualizados = np.dot(pontos, matriz_rotacao)
            novas_coordenadas.append(
                (
                    pontos_atualizados[0][0],
                    pontos_atualizados[0][1],
                    pontos_atualizados[0][2],
                )
            )
        elemento_grafico.set_coordenadas(novas_coordenadas)

        WindowOperations.translacao(elemento_grafico, (+Cx, +Cy, +Cz))

    @staticmethod
    def rotacao3DY(elemento_grafico, angulo):
        Cx, Cy, Cz = elemento_grafico.get_centro3D()
        WindowOperations.translacao(elemento_grafico, (-Cx, -Cy, -Cz))

        matriz_rotacao = np.array(
            [
                [cos(angulo), 0, -sin(angulo), 0],
                [0, 1, 0, 0],
                [sin(angulo), 0, cos(angulo), 0],
                [0, 0, 0, 1],
            ]
        )

        novas_coordenadas = []
        for i, j, k in elemento_grafico.get_coordenadas():
            pontos = np.array([[i, j, k, 1]])
            pontos_atualizados = np.dot(pontos, matriz_rotacao)
            novas_coordenadas.append(
                (
                    pontos_atualizados[0][0],
                    pontos_atualizados[0][1],
                    pontos_atualizados[0][2],
                )
            )
        elemento_grafico.set_coordenadas(novas_coordenadas)

        WindowOperations.translacao(elemento_grafico, (+Cx, +Cy, +Cz))

    @staticmethod
    def rotacao3DZ(elemento_grafico, angulo):
        Cx, Cy, Cz = elemento_grafico.get_centro3D()
        WindowOperations.translacao(elemento_grafico, (-Cx, -Cy, -Cz))

        matriz_rotacao = np.array(
            [
                [cos(angulo), sin(angulo), 0, 0],
                [-sin(angulo), cos(angulo), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )

        novas_coordenadas = []
        for i, j, k in elemento_grafico.get_coordenadas():
            pontos = np.array([[i, j, k, 1]])
            pontos_atualizados = np.dot(pontos, matriz_rotacao)
            novas_coordenadas.append(
                (
                    pontos_atualizados[0][0],
                    pontos_atualizados[0][1],
                    pontos_atualizados[0][2],
                )
            )
        elemento_grafico.set_coordenadas(novas_coordenadas)

        WindowOperations.translacao(elemento_grafico, (+Cx, +Cy, +Cz))
