class FormulasMatematicas:
    @staticmethod
    def calcular_x_viewport(X_window: float, X_win_min: float, X_win_max: float, X_vp_min: float, X_vp_max: float) -> float:
        return ((X_window - X_win_min)/(X_win_max - X_win_min))*(X_vp_max - X_vp_min)

    @staticmethod
    def calcular_y_viewport(Y_window: float, Y_win_min: float, Y_win_max: float, Y_vp_min: float, Y_vp_max: float) -> float:
        return (1 - ((Y_window - Y_win_min)/(Y_win_max - Y_win_min)))*(Y_vp_max - Y_vp_min)

    @staticmethod
    def transformada_viewport(X_window: float, X_win_min: float, X_win_max: float, X_vp_min: float, X_vp_max: float, 
                              Y_window: float, Y_win_min: float, Y_win_max: float, Y_vp_min: float, Y_vp_max: float) -> tuple:
        X_viewport = FormulasMatematicas.calcular_x_viewport(X_window, X_win_min, X_win_max, X_vp_min, X_vp_max)
        Y_viewport = FormulasMatematicas.calcular_y_viewport(Y_window, Y_win_min, Y_win_max, Y_vp_min, Y_vp_max)

        return(X_viewport, Y_viewport)
