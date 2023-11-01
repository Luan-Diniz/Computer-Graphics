class Config:
    @staticmethod
    # Define o menor valor negativo que um ponto pode ter
    def valorMinimoQDoubleSpinBox():
        return -99999999.99

    @staticmethod
    # Define o maior valor positivo que um ponto pode ter
    def valorMaximoQDoubleSpinBox():
        return 99999999.99

    # Valores iniciais da Window
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
    def window_rotation_angle():
        return 30  # 30 graus

    @staticmethod
    def scale():
        return 0.1
