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

        pass
        #TODO: Calcula as coordenadas normalizadas de todos os objetos.
        #1º Translada todo o mundo em (-Wcx, -Wcy)
        #2º Rotaciona todo mundo em -angulo Vup e Y.
        #3º ??? (Translada em (Wcx,Wcy)? e daí salva as coordenadas normalizadas?)
