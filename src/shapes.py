from elemento_grafico import ElementoGrafico


class Ponto(ElementoGrafico):
    def __init__(self, nome, coordenadas):
        super().__init__(nome=nome, tipo="Ponto", coordenadas=coordenadas)


class Reta(ElementoGrafico):
    def __init__(self, nome, coordenadas):
        super().__init__(nome=nome, tipo="Reta", coordenadas=coordenadas)


class Wireframe(ElementoGrafico):
    def __init__(self, nome, coordenadas):
        super().__init__(nome=nome, tipo="Wireframe", coordenadas=coordenadas)
