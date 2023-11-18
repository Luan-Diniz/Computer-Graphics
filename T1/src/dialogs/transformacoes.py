from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QComboBox,
    QDialog,
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from src.interface.config import Config


class TransformacoesDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.submitted = False
        self.transformacao = {"transformacao": "", "argumento": []}

        self.setWindowTitle("Transformações")
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(400, 300))
        self.setStyleSheet("background-color: rgb(165,165,165);")

        layout = QVBoxLayout()
        self.tab_widget = QTabWidget()

        # Instanciando as abas
        translacao = QWidget()
        rotacao = QWidget()
        escalonamento = QWidget()

        # Criando a aba da translacao
        translacao_layout = QFormLayout()
        translacao_layout.setVerticalSpacing(20)  # Espacamento vertical entre as linhas
        translacao_layout.setHorizontalSpacing(10)  # Espacamento horizontal

        # Botao cancelar
        cancel_button_1 = QPushButton("Cancelar")
        cancel_button_1.clicked.connect(self.close)
        cancel_button_1.setStyleSheet("background-color: rgb(212,208,200);")
        cancel_button_1.setFixedSize(150, 30)

        # Botao translacao
        translacao_button = QPushButton("OK")
        translacao_button.clicked.connect(self.translacao)
        translacao_button.setStyleSheet("background-color: rgb(212,208,200);")
        translacao_button.setFixedSize(150, 30)

        # Coordenada x translacao
        self.translacao_x = QDoubleSpinBox()
        self.translacao_x.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.translacao_x.setMaximum(Config.valorMaximoQDoubleSpinBox())
        self.translacao_x.setFixedSize(150, 30)

        # Coordenada y translacao
        self.translacao_y = QDoubleSpinBox()
        self.translacao_y.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.translacao_y.setMaximum(Config.valorMaximoQDoubleSpinBox())
        self.translacao_y.setFixedSize(150, 30)

        # Coordenada z translacao
        self.translacao_z = QDoubleSpinBox()
        self.translacao_z.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.translacao_z.setMaximum(Config.valorMaximoQDoubleSpinBox())
        self.translacao_z.setFixedSize(150, 30)

        # Layout translacao
        translacao_layout.addRow(QLabel("Desvio em X:"), self.translacao_x)
        translacao_layout.addRow(QLabel("Desvio em Y:"), self.translacao_y)
        translacao_layout.addRow(QLabel("Desvio em Z:"), self.translacao_z)
        translacao_layout.addRow(translacao_button, cancel_button_1)
        translacao.setLayout(translacao_layout)

        # Criando a aba da rotacao
        rotacao_label = QLabel("Ponto de Rotação:")
        rotacao_layout = QFormLayout()
        rotacao_layout.setVerticalSpacing(20)  # Espacamento vertical entre as linhas
        rotacao_layout.setHorizontalSpacing(10)  # Espacamento horizontal

        # Botao cancelar
        cancel_button_2 = QPushButton("Cancelar")
        cancel_button_2.clicked.connect(self.close)
        cancel_button_2.setStyleSheet("background-color: rgb(212,208,200);")
        cancel_button_2.setFixedSize(150, 30)

        # Botao rotacao
        rotacao_button = QPushButton("OK")
        rotacao_button.clicked.connect(self.rotacao)
        rotacao_button.setStyleSheet("background-color: rgb(212,208,200);")
        rotacao_button.setFixedSize(150, 30)

        # Combo box rotacao
        self.rotacao_opcoes = QComboBox()
        self.rotacao_opcoes.addItem("A Origem")
        self.rotacao_opcoes.addItem("Um Ponto")
        self.rotacao_opcoes.addItem("O Centro do Objeto")
        self.rotacao_opcoes.setFixedSize(150, 30)
        rotacao_layout.addRow(rotacao_label, self.rotacao_opcoes)

        # Angulo da rotacao
        self.rotacao_angulo = QDoubleSpinBox()
        self.rotacao_angulo.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.rotacao_angulo.setMaximum(Config.valorMaximoQDoubleSpinBox())
        self.rotacao_angulo.setFixedSize(150, 30)

        # Coordenada x rotacao
        self.rotacao_x = QDoubleSpinBox()
        self.rotacao_x.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.rotacao_x.setMaximum(Config.valorMaximoQDoubleSpinBox())
        self.rotacao_x.setFixedSize(150, 30)

        # Coordenada y rotacao
        self.rotacao_y = QDoubleSpinBox()
        self.rotacao_y.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.rotacao_y.setMaximum(Config.valorMaximoQDoubleSpinBox())
        self.rotacao_y.setFixedSize(150, 30)

        # Coordenada z rotacao
        self.rotacao_z = QDoubleSpinBox()
        self.rotacao_z.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.rotacao_z.setMaximum(Config.valorMaximoQDoubleSpinBox())
        self.rotacao_z.setFixedSize(150, 30)

        # Layout rotacao
        rotacao_layout.addRow(QLabel("Coordenada X do ponto: "), self.rotacao_x)
        rotacao_layout.addRow(QLabel("Coordenada Y do ponto: "), self.rotacao_y)
        rotacao_layout.addRow(QLabel("Coordenada Z do ponto: "), self.rotacao_z)
        rotacao_layout.addRow(QLabel("Ângulo da Rotação: "), self.rotacao_angulo)

        rotacao_layout.addRow(rotacao_button, cancel_button_2)
        rotacao.setLayout(rotacao_layout)

        # Criando a aba do escalonamento
        escalonamento_layout = QFormLayout()
        escalonamento_layout.setVerticalSpacing(
            20
        )  # Espacamento vertical entre as linhas
        escalonamento_layout.setHorizontalSpacing(10)  # Espacamento horizontal

        # Botao cancelar
        cancel_button_3 = QPushButton("Cancelar")
        cancel_button_3.clicked.connect(self.close)
        cancel_button_3.setStyleSheet("background-color: rgb(212,208,200);")
        cancel_button_3.setFixedSize(150, 30)

        # Botao escalonamento
        escalonamento_button = QPushButton("OK")
        escalonamento_button.clicked.connect(self.escalonamento)
        escalonamento_button.setStyleSheet("background-color: rgb(212,208,200);")
        escalonamento_button.setFixedSize(150, 30)

        # Valor do escalonamento
        self.escalonamento_valor = QDoubleSpinBox()
        self.escalonamento_valor.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.escalonamento_valor.setMaximum(Config.valorMaximoQDoubleSpinBox())
        self.escalonamento_valor.setFixedSize(150, 30)

        # Layout escalonamento
        escalonamento_layout.addRow(
            QLabel("Valor da escala: "), self.escalonamento_valor
        )
        escalonamento_layout.addRow(escalonamento_button, cancel_button_3)
        escalonamento.setLayout(escalonamento_layout)

        # Adicione as abas ao QTabWidget
        self.tab_widget.addTab(translacao, "Translação")
        self.tab_widget.addTab(rotacao, "Rotação")
        self.tab_widget.addTab(escalonamento, "Escalonamento")

        layout.addWidget(self.tab_widget)

        self.setLayout(layout)

    def accept(self):
        self.submitted = True
        self.close()

    def translacao(self):
        self.transformacao["transformacao"] = "translacao"
        self.transformacao["argumento"].append(
            (
                self.translacao_x.value(),
                self.translacao_y.value(),
                self.translacao_z.value(),
            )
        )
        self.accept()

    def rotacao(self):
        self.transformacao["transformacao"] = "rotacao"
        self.transformacao["argumento"].append(self.rotacao_angulo.value())
        if self.rotacao_opcoes.currentIndex() == 0:
            self.transformacao["argumento"].append((None, "origem"))
        elif self.rotacao_opcoes.currentIndex() == 1:
            self.transformacao["argumento"].append(
                (self.rotacao_x.value(), self.rotacao_y.value(), self.rotacao_z.value())
            )
        else:
            self.transformacao["argumento"].append((None, "centro_objeto"))

        self.accept()

    def escalonamento(self):
        self.transformacao["transformacao"] = "escalonamento"
        self.transformacao["argumento"].append(self.escalonamento_valor.value())
        self.accept()

    def aviso_escalonamento_zero(self):
        pedirNome = QMessageBox()
        pedirNome.setWindowTitle("Aviso!")
        pedirNome.setIcon(QMessageBox.Warning)
        pedirNome.setText("O valor do escalonamento não pode ser 0")
        pedirNome.setStyleSheet("background-color: rgb(165,165,165);")

        pedirNome.setStandardButtons(QMessageBox.Ok)
        botao_ok = pedirNome.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")

        x = pedirNome.exec_()
