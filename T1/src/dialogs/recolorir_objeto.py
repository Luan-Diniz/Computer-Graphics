from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel, QPushButton, QSpinBox


class RecolorirObjetoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.submitted = False

        self.setWindowTitle("Recolorir")
        self.formLayout = QFormLayout()

        self.setMinimumSize(QSize(215, 175))
        self.setMaximumSize(QSize(215, 175))
        self.setStyleSheet("background-color: rgb(165, 165, 165);")

        # Cria o label e a entrada para a cor R
        self.labelCorR = QLabel("<pre><b>    R</b></pre>")
        self.cor_R_objeto = QSpinBox()
        self.cor_R_objeto.setFixedSize(85, 30)
        self.formLayout.addRow(self.labelCorR, self.cor_R_objeto)
        self.cor_R_objeto.setMinimum(0)
        self.cor_R_objeto.setMaximum(255)

        # Cria o label e a entrada para a cor G
        self.labelCorG = QLabel("<pre><b>    G</b></pre>")
        self.cor_G_objeto = QSpinBox()
        self.cor_G_objeto.setFixedSize(85, 30)
        self.formLayout.addRow(self.labelCorG, self.cor_G_objeto)
        self.cor_G_objeto.setMinimum(0)
        self.cor_G_objeto.setMaximum(255)

        # Cria o label e a entrada para a cor B
        self.labelCorB = QLabel("<pre><b>    B</b></pre>")
        self.cor_B_objeto = QSpinBox()
        self.cor_B_objeto.setFixedSize(85, 30)
        self.formLayout.addRow(self.labelCorB, self.cor_B_objeto)
        self.cor_B_objeto.setMinimum(0)
        self.cor_B_objeto.setMaximum(255)

        button_ok = QPushButton("OK")
        button_ok.setStyleSheet("background-color: rgb(212,208,200);")
        button_ok.setFixedSize(85, 30)
        button_ok.clicked.connect(self.accept)

        button_cancel = QPushButton("Cancelar")
        button_cancel.setStyleSheet("background-color: rgb(212,208,200);")
        button_cancel.setFixedSize(85, 30)
        button_cancel.clicked.connect(self.close)

        self.formLayout.addRow(button_ok, button_cancel)

        self.setLayout(self.formLayout)

    def accept(self):
        self.submitted = True
        self.close()

    def cores(self):
        return (
            self.cor_R_objeto.value(),
            self.cor_G_objeto.value(),
            self.cor_B_objeto.value(),
        )
