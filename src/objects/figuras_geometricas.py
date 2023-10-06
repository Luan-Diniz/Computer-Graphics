from src.objects.elemento_grafico import ElementoGrafico


class Ponto(ElementoGrafico):
    def __init__(self, nome, cor, coordenadas):
        super().__init__(nome=nome, cor=cor, tipo="Ponto", coordenadas=coordenadas)


class Reta(ElementoGrafico):
    def __init__(self, nome, cor, coordenadas):
        super().__init__(nome=nome, cor=cor, tipo="Reta", coordenadas=coordenadas)


class Wireframe(ElementoGrafico):
    def __init__(self, nome, cor, coordenadas, preenchido):
        super().__init__(nome=nome, cor=cor, tipo="Wireframe", coordenadas=coordenadas)
        self.preenchido = preenchido


class Curva(ElementoGrafico):
    def __init__(self, nome, cor, coordenadas, pontos):
        super().__init__(nome=nome, cor=cor, tipo="Curva", coordenadas=coordenadas)
        self.pontos = pontos
