from math import fmod

from formulas_matematicas import *
from window import Window


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
        # Centro da Window
        (Wxc, Wyc) = window.getCenter()

        matriz_tras_ao_centro = FormulasMatematicas.cria_matriz_translacao(-Wxc, -Wyc)
        matriz_rotaciona = FormulasMatematicas.cria_matriz_rotacao(-window.currentAngle())  # Dentro da funcao vira radianos
        #matriz_devolve_onde_estava = FormulasMatematicas.cria_matriz_translacao(+Wxc, +Wyc)

        Sx = 1 / (0.5 * (window.Xwmax - window.Xwmin))
        Sy = 1 / (0.5 * (window.Ywmax - window.Ywmin))
        matriz_devolve_onde_estava = FormulasMatematicas.cria_matriz_escalonamento(Sx, Sy)

        matriz_resultante = FormulasMatematicas.junta_matrizes(
            matriz_tras_ao_centro, matriz_rotaciona, matriz_devolve_onde_estava
        )

        for elemento in self.lista_elementos_graficos:
            coordenadas = elemento.get_coordenadas()
            novas_coordenadas = []

            for x, y in coordenadas:
                pontos = np.array([[x, y, 1]])
                pontos_atualizados = np.dot(pontos, matriz_resultante)

                novas_coordenadas.append(pontos_atualizados.tolist()[0])
                # print(f"ANTES: {(x,y)}    DEPOIS: {pontos_atualizados.tolist()[0]}")

            elemento.set_coordenadas_normalizadas(
                novas_coordenadas
            )  # Atualiza as coordenadas normalizadas


    '''
        print("CHEGOU NOP TESTE")
        # teste

        matriz_transl1 = FormulasMatematicas.cria_matriz_translacao(-Wxc, -Wyc)
        matriz_rot = FormulasMatematicas.cria_matriz_rotacao(window.angle)
        matriz_transl2 = FormulasMatematicas.cria_matriz_translacao(Wxc, Wyc)
        matriz_resultante = FormulasMatematicas.junta_matrizes(matriz_transl1, matriz_rot, matriz_transl2)

        novos_pontos_minimos = np.dot(np.array([[window.Xwmin, window.Ywmin, 1]]), matriz_resultante)
        novos_pontos_maximos = np.dot(np.array([[window.Xwmax, window.Ywmax, 1]]), matriz_resultante)

        window.Xwmin, window.Ywmin = novos_pontos_minimos.tolist()[0][0:2]
        window.Xwmin, window.Ywmin = novos_pontos_maximos.tolist()[0][0:2]

        # fim do teste

        print("PASSOU NO TESTE")
    '''