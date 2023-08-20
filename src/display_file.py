from shapes import *


class DisplayFile:
    def __init__(self):
        self.lista_elementos_graficos = []


    def remover(self, i: int):
        self.lista_elementos_graficos.pop(i)
        """
        for i in range(len(self.lista_elementos_graficos)):
            if self.lista_elementos_graficos[i].get_nome() == nome:
                self.lista_elementos_graficos.pop(i)
        """

    def adicionar(self, elemento_grafico):
        self.lista_elementos_graficos.append(elemento_grafico)


    def getListaElementosGraficos(self):
        return self.lista_elementos_graficos

    def getNomesElementosGraficos(self):
        nomes = []
        for i in range(len(self.lista_elementos_graficos)):
            nomes.append(self.lista_elementos_graficos[i].get_nome())
        return nomes