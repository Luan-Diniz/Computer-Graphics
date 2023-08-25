from elemento_grafico import ElementoGrafico


class Ponto(ElementoGrafico):
    def __init__(self, nome, coordenadas):
        super().__init__(
            nome=nome, cor=(0, 0, 0), tipo="Ponto", coordenadas=coordenadas
        )


class Reta(ElementoGrafico):
    def __init__(self, nome, coordenadas):
        super().__init__(nome=nome, cor=(0, 0, 0), tipo="Reta", coordenadas=coordenadas)


class Wireframe(ElementoGrafico):
    def __init__(self, nome, coordenadas):
        super().__init__(
            nome=nome, cor=(0, 0, 0), tipo="Wireframe", coordenadas=coordenadas
        )
