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


class BSpline(ElementoGrafico):
    def __init__(self, nome, cor, coordenadas, pontos):
        super().__init__(nome=nome, cor=cor, tipo="B-Spline", coordenadas=coordenadas)
        self.pontos = pontos


class Objeto3D(ElementoGrafico):
    def __init__(self, nome, cor, coordenadas):
        super().__init__(nome=nome, cor=cor, tipo="Objeto 3D", coordenadas=coordenadas)


class Superficie3D(ElementoGrafico):
    def __init__(self, nome, cor, coordenadas):
        super().__init__(
            nome=nome, cor=cor, tipo="Superfície 3D", coordenadas=coordenadas
        )


class SuperficieBicubica(ElementoGrafico):
    def __init__(self, nome, cor, coordenadas):
        super().__init__(
            nome=nome, cor=cor, tipo="Superfície Bicúbica", coordenadas=coordenadas
        )
