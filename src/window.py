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
        tempXwmax = self.Xwmax
        tempXwmin = self.Xwmin

        self.Xwmin += (tempXwmax - tempXwmin) * self.scale
        self.Xwmax += (tempXwmax - tempXwmin) * self.scale

    def moveuEsquerda(self):
        tempXwmax = self.Xwmax
        tempXwmin = self.Xwmin

        self.Xwmin -= (tempXwmax - tempXwmin) * self.scale
        self.Xwmax -= (tempXwmax - tempXwmin) * self.scale

    def moveuCima(self):
        tempXwmax = self.Xwmax
        tempXwmin = self.Xwmin

        self.Ywmin += (tempXwmax - tempXwmin) * self.scale
        self.Ywmax += (tempXwmax - tempXwmin) * self.scale

    def moveuBaixo(self):
        tempXwmax = self.Xwmax
        tempXwmin = self.Xwmin

        self.Ywmin -= (tempXwmax - tempXwmin) * self.scale
        self.Ywmax -= (tempXwmax - tempXwmin) * self.scale

    def ZoomIn(self):
        # A Window fica menor, logo as imagens que ela ve sao "maiores"
        tempXwmax = self.Xwmax
        tempXwmin = self.Xwmin

        self.Xwmin += (tempXwmax - tempXwmin) * self.scale
        self.Xwmax -= (tempXwmax - tempXwmin) * self.scale
        self.Ywmin += (tempXwmax - tempXwmin) * self.scale
        self.Ywmax -= (tempXwmax - tempXwmin) * self.scale

    def ZoomOut(self):
        # A Window fica maior, logo as imagens que ela ve sao "menores"
        tempXwmax = self.Xwmax
        tempXwmin = self.Xwmin

        self.Xwmin -= (tempXwmax - tempXwmin) * self.scale
        self.Xwmax += (tempXwmax - tempXwmin) * self.scale
        self.Ywmin -= (tempXwmax - tempXwmin) * self.scale
        self.Ywmax += (tempXwmax - tempXwmin) * self.scale

    def getCenter(self) -> tuple:
        return ((self.Xwmax - self.Xwmin)/2, (self.Ywmax - self.Ywmin)/2)


    def rotateLeft(self):
        self.angle += Config.window_rotation_angle()

    def rotateRight(self):
        self.angle -= Config.window_rotation_angle()

    def currentAngle(self):
        return self.angle
    def setAngle(self, angulo):
        self.angle = angulo