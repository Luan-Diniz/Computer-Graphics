class ViewPort:
    """
    Os valores base da viewport não devem mudar, visto que o tamanho
    da janela e do frame viewport são fixos.
    """

    @staticmethod
    def viewport_dimensions():
        # O viewport tem o mesmo tamanho que o frame em ui_main_display.py
        return 10, 40, 411, 421  # X ,Y , width, height

    @staticmethod
    def viewportXmin():
        return ViewPort.viewport_dimensions()[0]

    @staticmethod
    def viewportXmax():
        return ViewPort.viewport_dimensions()[0] + ViewPort.viewport_dimensions()[2]

    @staticmethod
    def viewportYmin():
        return ViewPort.viewport_dimensions()[1]

    @staticmethod
    def viewportYmax():
        return ViewPort.viewport_dimensions()[1] + ViewPort.viewport_dimensions()[3]
