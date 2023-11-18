from src.interface.viewport import ViewPort
from src.interface.window import Window


class ViewportOperations:
    @staticmethod
    def calcular_x_viewport(Xw: float, window: Window) -> float:
        # Xw é uma coordenada X no sistema cartesiano da Window
        viewport_variance = ViewPort.viewportXmax() - ViewPort.viewportXmin()
        return (
            20
            + (
                (Xw - window.Xwminnormalizado)
                / (window.Xwmaxnormalizado - window.Xwminnormalizado)
            )
            * viewport_variance
        )

    @staticmethod
    def calcular_y_viewport(Yw: float, window: Window) -> float:
        # Yw é uma coordenada Y no sistema cartesiano da Window
        viewport_variance = ViewPort.viewportYmax() - ViewPort.viewportYmin()
        return (
            20
            + (
                1
                - (
                    (Yw - window.Ywminnormalizado)
                    / (window.Ywmaxnormalizado - window.Ywminnormalizado)
                )
            )
            * viewport_variance
        )

    @staticmethod
    def transformada_viewport(Xw: float, Yw: float, window: Window) -> tuple:
        X_viewport = ViewportOperations.calcular_x_viewport(Xw, window)
        Y_viewport = ViewportOperations.calcular_y_viewport(Yw, window)

        return (X_viewport, Y_viewport)
