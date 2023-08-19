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