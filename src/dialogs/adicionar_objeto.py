from PyQt5.QtCore import QMetaObject, QRect, QSize, Qt
from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMessageBox,
    QScrollArea,
    QSpinBox,
)

from src.interface.config import Config


class AdicionarObjetoDialog(QDialog):
    def __init__(self, qtdade_coordenadas: int, nomes_elementos_graficos: list):
        super().__init__()

        # Aqui estao armazenados todos os nomes dos elementos graficos atualmente existentes
        self.nomes_elementos_graficos = nomes_elementos_graficos

        # So sera "True" se o usuario clicar em "ok": a funcao accept() torna ele "True"
        self.submitted = False
        # Nesse dicionario serao armazenadas as informacoes do objeto que sera criado
        self.dict_info = {
            "nome": "",
            "cor": (),
            "coordenadas": [],
        }

        self.qtdade_coordenadas = qtdade_coordenadas
        self.setWindowTitle("Criar Objeto")

        self.resize(400, 300)
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(400, 300))
        self.setStyleSheet("background-color: rgb(165, 165, 165);")
        self.standard_buttons = QDialogButtonBox(self)
        self.standard_buttons.setGeometry(QRect(50, 260, 341, 32))
        self.standard_buttons.setStyleSheet("background-color: rgb(212,208,200);")
        self.standard_buttons.setOrientation(Qt.Horizontal)
        self.standard_buttons.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )
        self.standard_buttons.setObjectName("standard_buttons")

        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox()

        self.labelXList = []
        self.labelYList = []
        self.labelZList = []
        self.coordinateXList = []
        self.coordinateYList = []
        self.coordinateZList = []

        # Cria o label e a entrada para um nome
        self.labelNome = QLabel("Nome: ")
        self.nome_objeto = QLineEdit()
        self.formLayout.addRow(self.labelNome, self.nome_objeto)

        # Cria o label e a entrada para a cor R
        self.labelCorR = QLabel("R")
        self.cor_R_objeto = QSpinBox()
        self.formLayout.addRow(self.labelCorR, self.cor_R_objeto)
        self.cor_R_objeto.setMinimum(0)
        self.cor_R_objeto.setMaximum(255)

        # Cria o label e a entrada para a cor G
        self.labelCorG = QLabel("G")
        self.cor_G_objeto = QSpinBox()
        self.formLayout.addRow(self.labelCorG, self.cor_G_objeto)
        self.cor_G_objeto.setMinimum(0)
        self.cor_G_objeto.setMaximum(255)

        # Cria o label e a entrada para a cor B
        self.labelCorB = QLabel("B")
        self.cor_B_objeto = QSpinBox()
        self.formLayout.addRow(self.labelCorB, self.cor_B_objeto)
        self.cor_B_objeto.setMinimum(0)
        self.cor_B_objeto.setMaximum(255)

        # Cria os QDoubleSpinBox para entrada numerica
        for i in range(0, self.qtdade_coordenadas):
            self.labelXList.append(QLabel(f"X{i + 1}"))
            self.coordinateXList.append(QDoubleSpinBox())
            self.labelYList.append(QLabel(f"Y{i + 1}"))
            self.coordinateYList.append(QDoubleSpinBox())
            self.labelZList.append(QLabel(f"Z{i + 1}"))
            self.coordinateZList.append(QDoubleSpinBox())
            self.formLayout.addRow(self.labelXList[i], self.coordinateXList[i])
            self.formLayout.addRow(self.labelYList[i], self.coordinateYList[i])
            self.formLayout.addRow(self.labelZList[i], self.coordinateZList[i])

            # Seta o range de numeros que o QDoubleSpinBox aceita
            self.coordinateXList[i].setMinimum(Config.valorMinimoQDoubleSpinBox())
            self.coordinateYList[i].setMinimum(Config.valorMinimoQDoubleSpinBox())
            self.coordinateZList[i].setMinimum(Config.valorMinimoQDoubleSpinBox())
            self.coordinateXList[i].setMaximum(Config.valorMaximoQDoubleSpinBox())
            self.coordinateYList[i].setMaximum(Config.valorMaximoQDoubleSpinBox())
            self.coordinateZList[i].setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.groupBox.setLayout(self.formLayout)

        # Scroll bar
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(QRect(20, 20, 351, 241))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidget(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.standard_buttons.accepted.connect(self.accept)  # type: ignore
        self.standard_buttons.rejected.connect(self.reject)  # type: ignore
        QMetaObject.connectSlotsByName(self)

    def accept(self):  # Sobreescrita do metodo do botao accept
        nome = self.nome_objeto.text()

        if nome in self.nomes_elementos_graficos:
            self.nome_repetido()

        elif len(nome.replace(" ", "")) == 0:
            self.pedir_nome()
        else:
            self.dict_info["nome"] = nome
            self.dict_info["cor"] = (
                self.cor_R_objeto.value(),
                self.cor_G_objeto.value(),
                self.cor_B_objeto.value(),
            )
            for i in range(0, self.qtdade_coordenadas):
                self.dict_info["coordenadas"].append(
                    (
                        self.coordinateXList[i].value(),
                        self.coordinateYList[i].value(),
                        self.coordinateZList[i].value(),
                    )
                )

            self.submitted = True

            self.close()  # Fecha a window

    def pedir_nome(self):
        pedirNome = QMessageBox()
        pedirNome.setWindowTitle("Aviso!")
        pedirNome.setIcon(QMessageBox.Warning)
        pedirNome.setText("O objeto precisa ter um nome")
        pedirNome.setStyleSheet("background-color: rgb(165,165,165);")

        pedirNome.setStandardButtons(QMessageBox.Ok)
        botao_ok = pedirNome.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")

        x = pedirNome.exec_()

    def nome_repetido(self):
        nome_repetido = QMessageBox()
        nome_repetido.setWindowTitle("Aviso!")
        nome_repetido.setIcon(QMessageBox.Warning)
        nome_repetido.setText("Já existe um objeto com esse nome")
        nome_repetido.setStyleSheet("background-color: rgb(165,165,165);")

        nome_repetido.setStandardButtons(QMessageBox.Ok)
        botao_ok = nome_repetido.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")

        x = nome_repetido.exec_()
