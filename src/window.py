from config import Config


class Window:
    def __init__(self):
        # Coordenadas do mundo real
        self.Xwmin = Config.window_Xwmin()
        self.Xwmax = Config.window_Xwmax()
        self.Ywmin = Config.window_Ywmin()
        self.Ywmax = Config.window_Ywmax()
        self.scale = Config.scale()

        self.angle = 0  #Em graus

    def moveuDireita(self):
        deltax =  self.Xwmax - self.Xwmin

        self.Xwmin += (deltax) * self.scale
        self.Xwmax += (deltax) * self.scale

        print(self.getCenter())

    def moveuEsquerda(self):
        deltax =  self.Xwmax - self.Xwmin

        self.Xwmin -= (deltax) * self.scale
        self.Xwmax -= (deltax) * self.scale

        print(self.getCenter())

    def moveuCima(self):
        deltay = self.Ywmax - self.Ywmin

        self.Ywmin += (deltay) * self.scale
        self.Ywmax += (deltay) * self.scale

        print(self.getCenter())

    def moveuBaixo(self):
        deltay = self.Ywmax - self.Ywmin

        self.Ywmin -= (deltay) * self.scale
        self.Ywmax -= (deltay) * self.scale

        print(self.getCenter())

    def ZoomIn(self):
        # A Window fica menor, logo as imagens que ela ve sao "maiores"
        deltax = self.Xwmax - self.Xwmin
        deltay = self.Ywmax - self.Ywmin

        self.Xwmin += (deltax) * self.scale
        self.Xwmax -= (deltax) * self.scale
        self.Ywmin += (deltay) * self.scale
        self.Ywmax -= (deltay) * self.scale

        print(self.getCenter())

    def ZoomOut(self):
        # A Window fica maior, logo as imagens que ela ve sao "menores"
        deltax = self.Xwmax - self.Xwmin
        deltay = self.Ywmax - self.Ywmin

        self.Xwmin -= (deltax) * self.scale
        self.Xwmax += (deltax) * self.scale
        self.Ywmin -= (deltay) * self.scale
        self.Ywmax += (deltay) * self.scale

        print(self.getCenter())

    def getCenter(self) -> tuple:
        return ((self.Xwmax - self.Xwmin)/2, (self.Ywmax - self.Ywmin)/2)


    def rotacionaAntiHorario(self):
        self.angle += Config.window_rotation_angle()

    def rotatacionaHorario(self):
        self.angle -= Config.window_rotation_angle()

    def currentAngle(self):
        return self.angle

    def setAngle(self, angulo):
        self.angle = angulo


    def printCenter(self):
        print(self.getCenter())