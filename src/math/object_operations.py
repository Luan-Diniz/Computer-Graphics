from math import cos, radians, sin

import numpy as np

from src.math.window_operations import WindowOperations


class ObjectOperations:
    @staticmethod
    def translacao(elemento_grafico, coordinates):
        coordenadas_atualizadas = []
        (desvio_x, desvio_y) = coordinates

        matriz_translacao = np.array([[1, 0, 0], [0, 1, 0], [desvio_x, desvio_y, 1]])

        for i, j in elemento_grafico.get_coordenadas():
            pontos = np.array([[i, j, 1]])
            pontos_atualizados = np.dot(pontos, matriz_translacao)

            coordenadas_atualizadas.append(
                (pontos_atualizados[0][0], pontos_atualizados[0][1])
            )

        # Atualiza as coordenadas
        elemento_grafico.set_coordenadas(coordenadas_atualizadas)

    @staticmethod
    def rotacao(elemento_grafico, angle, coordinates):
        coordenadas_atualizadas = []
        angulo = radians(-angle)  # Angulo em radianos
        (x_rot, y_rot) = coordinates
        dx, dy = (None, None)  # desvios.

        if y_rot == "origem":
            dx, dy = 0, 0
        elif y_rot == "centro_objeto":
            (cx, cy) = elemento_grafico.get_centro()
            dx, dy = cx, cy
        else:
            # Funciona
            dx = x_rot
            dy = y_rot

        matriz_translacao1 = np.array([[1, 0, 0], [0, 1, 0], [-dx, -dy, 1]])

        matriz_rotacao = np.array(
            [
                [cos(angulo), -sin(angulo), 0],
                [sin(angulo), cos(angulo), 0],
                [0, 0, 1],
            ]
        )

        matriz_translacao2 = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])

        matriz_resultante = WindowOperations.junta_matrizes(
            matriz_translacao1, matriz_rotacao, matriz_translacao2
        )

        for i, j in elemento_grafico.get_coordenadas():
            pontos = np.array([[i, j, 1]])
            pontos_atualizados = np.dot(pontos, matriz_resultante)

            coordenadas_atualizadas.append(
                (pontos_atualizados[0][0], pontos_atualizados[0][1])
            )

        # Atualiza as coordenadas
        elemento_grafico.set_coordenadas(coordenadas_atualizadas)

    @staticmethod
    def escalonamento(elemento_grafico, coef_escalonamento):
        coordenadas_atualizadas = []
        (cx, cy) = elemento_grafico.get_centro()

        if coef_escalonamento == 0:
            return -1

        matriz_traz_ao_centro = np.array([[1, 0, 0], [0, 1, 0], [-cx, -cy, 1]])
        matriz_escalona = np.array(
            [
                [coef_escalonamento, 0, 0],
                [0, coef_escalonamento, 0],
                [0, 0, 1],
            ]
        )
        matriz_devolve_ao_local_original = np.array([[1, 0, 0], [0, 1, 0], [cx, cy, 1]])

        matriz_resultante = WindowOperations.junta_matrizes(
            matriz_traz_ao_centro,
            matriz_escalona,
            matriz_devolve_ao_local_original,
        )

        for i, j in elemento_grafico.get_coordenadas():
            pontos = np.array([[i, j, 1]])
            pontos_atualizados = np.dot(pontos, matriz_resultante)

            coordenadas_atualizadas.append(
                (pontos_atualizados[0][0], pontos_atualizados[0][1])
            )

        # Atualiza as coordenadas
        elemento_grafico.set_coordenadas(coordenadas_atualizadas)

    # --- Bezier ------------------------------------------------------------------------------------------ #
    def bezier(
        ponto_inicial,
        primeiro_controle,
        segundo_controle,
        pronto_final,
        quantidade_de_pontos,
    ):
        pontos_da_curva = []

        for t in range(int(quantidade_de_pontos) + 1):
            t /= quantidade_de_pontos
            x = (
                (1 - t) ** 3 * ponto_inicial[0]
                + 3 * (1 - t) ** 2 * t * primeiro_controle[0]
                + 3 * (1 - t) * t**2 * segundo_controle[0]
                + t**3 * pronto_final[0]
            )
            y = (
                (1 - t) ** 3 * ponto_inicial[1]
                + 3 * (1 - t) ** 2 * t * primeiro_controle[1]
                + 3 * (1 - t) * t**2 * segundo_controle[1]
                + t**3 * pronto_final[1]
            )
            pontos_da_curva.append((x, y))

        return pontos_da_curva
