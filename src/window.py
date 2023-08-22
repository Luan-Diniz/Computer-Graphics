from config import Config


class Window:
    def __init__(self):
        # Coordenadas do mundo real
        self.Xwmin = Config.window_Xwmin()
        self.Xwmax = Config.window_Xwmax()
        self.Ywmin = Config.window_Ywmin()
        self.Ywmax = Config.window_Ywmax()
        self.scale = Config.scale()

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
