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

from src.interface.config import Config


class QuantidadeDePontosDialog(QDialog):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo
        self.submitted = False
        self.setWindowTitle("Criar Objeto")
        self.setStyleSheet("background-color: rgb(165, 165, 165);")

        if self.tipo == "Wireframe":
            self.setMinimumSize(QSize(300, 100))
            self.setMaximumSize(QSize(300, 100))
        elif self.tipo == "B-Spline":
            self.setMinimumSize(QSize(350, 150))
            self.setMaximumSize(QSize(350, 150))
        elif self.tipo == "Objeto 3D":
            self.setMinimumSize(QSize(500, 150))
            self.setMaximumSize(QSize(500, 150))

        label_text = ""
        box_text = ""
        self.number_input = QSpinBox()
        if self.tipo == "Wireframe":
            label_text = "Escolha a quantidade de pontos do Polígono:"
            box_text = "Preencher polígono"
            self.number_input.setMinimum(3)
            self.number_input.setMaximum(int(Config.valorMaximoQDoubleSpinBox()))
        elif self.tipo == "B-Spline":
            label_text = "Quantidade de pontos de controle da B-Spline:"
            box_text = "Quantidade de pontos para a precisão da B-Spline:"
            self.number_input.setMinimum(4)
            self.number_input.setMaximum(int(Config.valorMaximoQDoubleSpinBox()))
        elif self.tipo == "Objeto 3D":
            label_text = "Quantidade arestas do Objeto 3D:"
            box_text = "As arestas começam nos pontos de índice par e terminam nos de índice ímpar\n\nEscolha as arestas na forma: (X1, Y1, Z1) -> (X2, Y2, Z2)"
            self.number_input.setMinimum(1)
            self.number_input.setMaximum(int(Config.valorMaximoQDoubleSpinBox()))

        self.label = QLabel(label_text)
        if self.tipo == "Wireframe":
            self.extra = QCheckBox(box_text)
        elif self.tipo == "B-Spline":
            self.extra = QSpinBox()
            self.extra.setMinimum(10)
            self.extra.setMaximum(int(Config.valorMaximoQDoubleSpinBox()))
        elif self.tipo == "Objeto 3D":
            self.extra = QLabel(box_text)

        button_ok = QPushButton("OK")
        button_ok.setStyleSheet("background-color: rgb(212,208,200);")
        button_ok.clicked.connect(self.accept)
        button_ok.setFixedSize(85, 30)

        vertical_layout = QVBoxLayout()

        horizontal_layout = QHBoxLayout()  # Layout horizontal para widgets lado a lado

        if self.tipo == "B-Spline":
            vertical_layout.addWidget(QLabel(box_text))
        vertical_layout.addWidget(self.extra)
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

    def get_extra(self):
        if self.tipo == "Wireframe":
            return self.extra.isChecked()
        elif self.tipo == "B-Spline":
            return self.extra.value()
        elif self.tipo == "Objeto 3D":
            return ""
