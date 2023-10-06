from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QCheckBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
)


class QuantidadeDePontosDialog(QDialog):
    def __init__(self, curva):
        super().__init__()
        self.submitted = False

        self.tipo = "o Polígono"
        if curva:
            self.tipo = "a Curva"

        self.setWindowTitle("Criar Objeto")
        self.setMinimumSize(QSize(300, 100))
        self.setMaximumSize(QSize(300, 100))
        self.setStyleSheet("background-color: rgb(165, 165, 165);")

        self.label = QLabel(f"Escolha a quantidade de pontos d{self.tipo}:")
        self.number_input = QSpinBox()
        self.number_input.setMinimum(3)

        if self.tipo == "o Polígono":
            self.preenchido = QCheckBox("Preencher polígono.")

        button_ok = QPushButton("OK")
        button_ok.setStyleSheet("background-color: rgb(212,208,200);")
        button_ok.clicked.connect(self.accept)
        button_ok.setFixedSize(85, 30)

        vertical_layout = QVBoxLayout()

        horizontal_layout = QHBoxLayout()  # Layout horizontal para widgets lado a lado

        if self.tipo == "o Polígono":
            vertical_layout.addWidget(self.preenchido)

        vertical_layout.addWidget(self.label)
        horizontal_layout.addWidget(self.number_input)
        horizontal_layout.addWidget(button_ok)

        vertical_layout.addLayout(
            horizontal_layout  # Adiciona o layout horizontal ao layout vertical
        )

        self.setLayout(vertical_layout)

    def accept(self):
        self.submitted = True
        self.close()

    def numero_pontos(self):
        return self.number_input.value()

    def poligono_preenchido(self):
        if self.tipo == "a Curva":
            return False
        return self.preenchido.isChecked()
