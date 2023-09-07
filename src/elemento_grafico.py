class ElementoGrafico:
    def __init__(self, nome: str, cor: tuple, tipo: str, coordenadas: list) -> None:
        self.nome = nome
        self.cor = cor
        self.tipo = tipo
        self.coordenadas = coordenadas  #lista de tuplas
        self.coordenadas_normalizadas = []

    def set_nome(self, nome: str) -> None:
        self.nome = nome

    def get_nome(self) -> str:
        return self.nome

    def set_cor(self, cor: tuple) -> None:
        self.cor = cor

    def get_cor(self) -> tuple:
        return self.cor

    def set_tipo(self, tipo: str) -> None:
        self.tipo = tipo

    def get_tipo(self) -> str:
        return self.tipo

    def set_coordenadas(self, coordenadas: list) -> None:
        self.coordenadas = coordenadas

    def get_coordenadas(self) -> list:
        return self.coordenadas

    def set_coordenadas_normalizadas(self, coordenadas_normalizadas):
        self.coordenadas_normalizadas = coordenadas_normalizadas

    def get_coordenadas_normalizadas(self) -> list:
        return self.coordenadas_normalizadas



    def add_ponto(self, novo_ponto: tuple) -> None:
        self.coordenadas.append(novo_ponto)


    def get_centro(self) -> tuple:
        cx = 0
        cy = 0

        for i,j in self.coordenadas_normalizadas:
            cx += i
            cy += j

        n_pontos = len(self.coordenadas_normalizadas)

        cx = cx/n_pontos
        cy = cy/n_pontos

        return (cx, cy)
