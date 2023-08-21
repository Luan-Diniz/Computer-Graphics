from config import Config
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDoubleSpinBox,
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class AdicionarDialog(QDialog):
    def __init__(self, qtdade_coordenadas: int, nomes_elementos_graficos: list):
        super().__init__()

        # Aqui estao armazenados todos os nomes dos elementos graficos atualmente existentes
        self.nomes_elementos_graficos = nomes_elementos_graficos

        # So sera "True" se o usuario clicar em "ok": a funcao accept() torna ele "True"
        self.submitted = False
        # Nesse dicionario serao armazenadas as informacoes do objeto que sera criado
        self.dict_info = {
            "nome": "",
            "coordenadas": [],
        }

        self.qtdade_coordenadas = qtdade_coordenadas
        self.setWindowTitle("Criar Objeto")

        self.resize(400, 300)
        self.setMinimumSize(QtCore.QSize(400, 300))
        self.setMaximumSize(QtCore.QSize(400, 300))
        self.setStyleSheet("background-color: rgb(165, 165, 165);")
        self.standard_buttons = QtWidgets.QDialogButtonBox(self)
        self.standard_buttons.setGeometry(QtCore.QRect(50, 260, 341, 32))
        self.standard_buttons.setStyleSheet("background-color: rgb(212,208,200);")
        self.standard_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.standard_buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.standard_buttons.setObjectName("standard_buttons")

        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox()

        self.labelXList = []
        self.labelYList = []
        self.coordinateXList = []
        self.coordinateYList = []

        # Cria o label e a entrada para um nome
        self.labelNome = QLabel("Nome: ")
        self.nome_objeto = QLineEdit()
        self.formLayout.addRow(self.labelNome, self.nome_objeto)

        # Cria os QDoubleSpinBox para entrada numerica
        for i in range(0, self.qtdade_coordenadas):
            self.labelXList.append(QLabel(f"X{i + 1}"))
            self.coordinateXList.append(QDoubleSpinBox())
            self.labelYList.append(QLabel(f"Y{i + 1}"))
            self.coordinateYList.append(QDoubleSpinBox())
            self.formLayout.addRow(self.labelXList[i], self.coordinateXList[i])
            self.formLayout.addRow(self.labelYList[i], self.coordinateYList[i])

            # Seta o range de numeros que o QDoubleSpinBox aceita
            self.coordinateXList[i].setMinimum(Config.valorMinimoQDoubleSpinBox())
            self.coordinateYList[i].setMinimum(Config.valorMinimoQDoubleSpinBox())
            self.coordinateXList[i].setMaximum(Config.valorMaximoQDoubleSpinBox())
            self.coordinateYList[i].setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.groupBox.setLayout(self.formLayout)

        # Scroll bar
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 351, 241))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidget(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.standard_buttons.accepted.connect(self.accept)  # type: ignore
        self.standard_buttons.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def accept(self):  # Sobreescrita do metodo do botao accept
        nome = self.nome_objeto.text()

        if nome in self.nomes_elementos_graficos:
            self.nome_repetido()

        elif len(nome.replace(" ", "")) == 0:
            self.pedir_nome()
        else:
            self.dict_info["nome"] = nome
            for i in range(0, self.qtdade_coordenadas):
                self.dict_info["coordenadas"].append(
                    (self.coordinateXList[i].value(), self.coordinateYList[i].value())
                )

            self.submitted = True

            self.close()  # Fecha a window

    def pedir_nome(self):
        pedirNome = QMessageBox()
        pedirNome.setWindowTitle("Aviso!")
        pedirNome.setIcon(QMessageBox.Warning)
        pedirNome.setText("O objeto precisa ter um nome")

        x = pedirNome.exec_()

    def nome_repetido(self):
        nome_repetido = QMessageBox()
        nome_repetido.setWindowTitle("Aviso!")
        nome_repetido.setIcon(QMessageBox.Warning)
        nome_repetido.setText("Já existe um objeto com esse nome")

        x = nome_repetido.exec_()


class OperacoesDialog(QDialog):
    def __init__(self):
        super().__init__()
        pass


class numero_pontosDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.submitted = False

        self.setWindowTitle("Criar Objeto")
        layout = QVBoxLayout()

        self.label = QLabel("Escolha a quantidade de pontos do Polígono:")
        self.number_input = QSpinBox()
        self.number_input.setMinimum(3)

        button_ok = QPushButton("OK")

        button_ok.clicked.connect(self.accept)

        layout.addWidget(self.label)
        layout.addWidget(self.number_input)
        layout.addWidget(button_ok)

        self.setLayout(layout)

    def accept(self):
        self.submitted = True
        self.close()

    def numero_pontos(self):
        return self.number_input.value()
