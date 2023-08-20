class Config():
    @staticmethod
    #Define o menor valor negativo que um ponto pode ter
    def valorMinimoQDoubleSpinBox():
        return -1e10

    #Valores iniciais da Window
    @staticmethod
    def window_Xwmin():
        return -100
    @staticmethod
    def window_Ywmin():
        return -100
    @staticmethod
    def window_Xwmax():
        return 100
    @staticmethod
    def window_Ywmax():
        return 100
    @staticmethod
    def window_offset():   #O quanto a window se move por clique
        return 50
    @staticmethod
    def window_zoom_offset():  # O quanto a window amplia/encolhe
        return 75



