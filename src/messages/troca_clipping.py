from PyQt5.QtWidgets import QMessageBox


class TrocaClipping(QMessageBox):
    def __init__(self, clipping_atual: str):
        super().__init__()
        self.setWindowTitle("Aviso!")
        self.setText(f"Agora o {clipping_atual.upper()} será o algoritmo de clipping utilizado.")
        self.setStyleSheet("background-color: rgb(212,208,200);")
        self.setStandardButtons(QMessageBox.Ok)
        botao_ok = self.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")
        self.setIcon(QMessageBox.Information)
