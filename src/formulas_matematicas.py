from viewport import ViewPort
from window import Window


class FormulasMatematicas:
    @staticmethod
    def calcular_x_viewport(Xw: float, window: Window) -> float:
        # Xw é uma coordenada X no sistema cartesiano da Window
        viewport_variance = ViewPort.viewportXmax() - ViewPort.viewportXmin()
        return ((Xw - window.Xwmin) / (window.Xwmax - window.Xwmin)) * viewport_variance

    @staticmethod
    def calcular_y_viewport(Yw: float, window: Window) -> float:
        # Yw é uma coordenada Y no sistema cartesiano da Window
        viewport_variance = ViewPort.viewportYmax() - ViewPort.viewportYmin()
        return (
            1 - ((Yw - window.Ymin) / (window.Ymax - window.Ymin))
        ) * viewport_variance

    @staticmethod
    def transformada_viewport(Xw: float, Yw: float, window: Window) -> tuple:
        X_viewport = FormulasMatematicas.calcular_x_viewport(Xw, window)
        Y_viewport = FormulasMatematicas.calcular_y_viewport(Yw, window)

        return (X_viewport, Y_viewport)
