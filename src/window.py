from config import Config

class Window():
    def __init__(self):
        #Coordenadas do mundo real
        self.Xwmin = Config.window_Xwmin()
        self.Xwmax = Config.window_Xwmax()
        self.Ywmin = Config.window_Ywmin()
        self.Ywmax = Config.window_Ywmax()

        self.__offset = Config.window_offset()
        self.__zoom_offset = Config.window_zoom_offset()



    def moveuDireita(self):
        self.Xwmin += self.__offset
        self.Xwmax += self.__offset
    def moveuEsquerda(self):
        self.Xwmin -= self.__offset
        self.Xwmax -= self.__offset
    def moveuCima(self):
        self.Ywmin += self.__offset
        self.Ywmax += self.__offset
    def moveuBaixo(self):
        self.Ywmin -= self.__offset
        self.Ywmax -= self.__offset

    def ZoomIn(self):
        #A Window fica menor. Logo as imagens que ela vê são "maiores"
        self.Xwmin += self.__zoom_offset
        self.Xwmax -= self.__zoom_offset
        self.Ywmin += self.__zoom_offset
        self.Ywmax -= self.__zoom_offset
    def ZoomOut(self):
        # A Window fica maior. Logo as imagens que ela vê são "menores"
        self.Xwmin -= self.__zoom_offset
        self.Xwmax += self.__zoom_offset
        self.Ywmin -= self.__zoom_offset
        self.Ywmax += self.__zoom_offset


