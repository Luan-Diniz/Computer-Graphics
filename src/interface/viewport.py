class ViewPort:
    """
    Os valores base da viewport não devem mudar, visto que o tamanho
    da janela e do frame viewport são fixos.
    """

    @staticmethod
    def viewport_dimensions():
        return 10, 40, 451, 461  # X ,Y , width, height

    @staticmethod
    def viewportXmin():
        return 10

    @staticmethod
    def viewportXmax():
        return 10 + 451

    @staticmethod
    def viewportYmin():
        return 40

    @staticmethod
    def viewportYmax():
        return 40 + 461
