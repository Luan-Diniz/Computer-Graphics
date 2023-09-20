from PyQt5.QtWidgets import QMessageBox


class ExtensaoInvalidaMessage(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aviso!")
        self.setText("O arquivo não possui extensão .obj ou .mtl")
        self.setStyleSheet("background-color: rgb(212,208,200);")
        self.setStandardButtons(QMessageBox.Ok)
        botao_ok = self.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")
        self.setIcon(QMessageBox.Warning)
