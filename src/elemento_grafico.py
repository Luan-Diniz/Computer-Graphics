class ElementoGrafico:
    def __init__(self, nome: str, tipo: str, coordenadas: list) -> None:
        self.nome = nome
        self.tipo = tipo
        self.coordenadas = coordenadas

    def set_nome(self, nome: str) -> None:
        self.nome = nome

    def get_nome(self) -> str:
        return self.nome

    def set_tipo(self, tipo: str) -> None:
        self.tipo = tipo

    def get_tipo(self) -> str:
        return self.tipo

    def set_coordenadas(self, coordenadas: list) -> None:
        self.coordenadas = coordenadas

    def get_coordenadas(self) -> list:
        return self.coordenadas

    def add_ponto(self, novo_ponto: tuple) -> None:
        self.coordenadas.append(novo_ponto)
