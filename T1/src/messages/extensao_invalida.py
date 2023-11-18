from PyQt5.QtWidgets import QMessageBox


class ExtensaoInvalidaMessage(QMessageBox):
    def __init__(self, nome_arquivo: str, nome_extensao: str):
        super().__init__()
        self.setWindowTitle("Aviso!")
        self.setText(f"O arquivo {nome_arquivo} não possui extensão {nome_extensao}")
        self.setStyleSheet("background-color: rgb(212,208,200);")
        self.setStandardButtons(QMessageBox.Ok)
        botao_ok = self.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")
        self.setIcon(QMessageBox.Warning)
