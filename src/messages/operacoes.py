from PyQt5.QtWidgets import QMessageBox


class OperacoesMessage(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operações")
        self.setText("Escolha a operação a ser realizada")
        self.setStyleSheet("background-color: rgb(165,165,165);")

        # Criando os botoes
        self.setStandardButtons(
            QMessageBox.Ok | QMessageBox.Save | QMessageBox.Open | QMessageBox.Abort | QMessageBox.Cancel
        )

        # Renomeando o botao de troca de cor
        botao_cor = self.button(QMessageBox.Ok)
        botao_cor.setText("Recolorir Objeto")
        botao_cor.setFixedSize(150, 30)
        botao_cor.setStyleSheet("background-color: rgb(212,208,200);")

        # Renomeando o botao de realizar transformacao 2D
        botao_transformacao = self.button(QMessageBox.Save)
        botao_transformacao.setText("Transformações 2D")
        botao_transformacao.setFixedSize(150, 30)
        botao_transformacao.setStyleSheet("background-color: rgb(212,208,200);")

        #Renomeando o botao de trocar metodo de clipping
        botao_transformacao = self.button(QMessageBox.Abort)
        botao_transformacao.setText("Trocar Clipping")
        botao_transformacao.setFixedSize(150, 30)
        botao_transformacao.setStyleSheet("background-color: rgb(212,208,200);")

        # Renomeando o botao de deletar objeto
        botao_deletar = self.button(QMessageBox.Open)
        botao_deletar.setText("Deletar Objeto")
        botao_deletar.setFixedSize(150, 30)
        botao_deletar.setStyleSheet("background-color: rgb(212,208,200);")

        # Renomeando o botao de cancelar
        botao_cancelar = self.button(QMessageBox.Cancel)
        botao_cancelar.setText("Cancelar")
        botao_cancelar.setFixedSize(150, 30)
        botao_cancelar.setStyleSheet("background-color: rgb(212,208,200);")

        self.setDefaultButton(QMessageBox.Cancel)
