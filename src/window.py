from config import Config

class Window():
    def __init__(self):
        #Coordenadas do mundo real
        self.Xwmin = Config.window_Xwmin()
        self.Xwmax = Config.window_Xwmax()
        self.Ymin = Config.window_Ywmin()
        self.Ymax = Config.window_Ywmax()

        self.__offset = Config.window_offset()



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

    #TODO:
    def ZoomIn(self):
        pass
    def ZoomOut(self):
        pass


