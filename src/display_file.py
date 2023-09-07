from window import Window
from formulas_matematicas import *

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
        #TODO: Calcula as coordenadas normalizadas de todos os objetos.
        #1º Translada todo o mundo em (-Wcx, -Wcy)
        #2º Rotaciona todo mundo em -angulo Vup e Y.
        #3º ??? (Translada em (Wcx,Wcy)? e daí salva as coordenadas normalizadas?)


        #Centro da Window
        (Wxc,Wyc) = window.getCenter()

        matriz_tras_ao_centro = FormulasMatematicas.cria_matriz_translacao(-Wxc, -Wyc)
        matriz_rotaciona = FormulasMatematicas.cria_matriz_rotacao(-window.currentAngle())
        matriz_devolve_onde_estava = FormulasMatematicas.cria_matriz_translacao(+Wxc, +Wyc)

        matriz_resultante = FormulasMatematicas.junta_matrizes(matriz_tras_ao_centro, matriz_rotaciona
                                                               , matriz_devolve_onde_estava)


        for elemento in self.lista_elementos_graficos:
            coordenadas = elemento.get_coordenadas()
            novas_coordenadas = []

            for (x,y) in coordenadas:
                pontos = np.array([[x, y, 1]])
                pontos_atualizados = np.dot(pontos, matriz_resultante)
                novas_coordenadas.append(pontos_atualizados)

            elemento.set_coordenadas_normalizadas(novas_coordenadas)  #Atualiza as coordenadas normalizadas




