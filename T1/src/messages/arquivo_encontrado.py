from PyQt5.QtWidgets import QMessageBox


class ArquivoEncontradoMessage(QMessageBox):
    def __init__(self, nome_arquivo: str):
        super().__init__()
        self.setWindowTitle("Atenção!")
        self.setText(f"O arquivo {nome_arquivo} será sobrescrito")
        self.setStyleSheet("background-color: rgb(165,165,165);")
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        botao_ok = self.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")
        botao_cancel = self.button(QMessageBox.Cancel)
        botao_cancel.setStyleSheet("background-color: rgb(212,208,200);")
        self.setIcon(QMessageBox.Information)
