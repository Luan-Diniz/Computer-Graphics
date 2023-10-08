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


class AdicionarCurvaDialog(QDialog):
    def __init__(self, nomes_elementos_graficos: list):
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
            "numero_de_pontos": 2,
        }

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

        self.label_numero_pontos = QLabel("Número de Pontos:")

        self.spin_box_numero_pontos = QSpinBox()
        self.spin_box_numero_pontos.setMinimum(2)
        self.spin_box_numero_pontos.setMaximum(int(Config.valorMaximoQDoubleSpinBox()))

        self.formLayout.addRow(self.label_numero_pontos, self.spin_box_numero_pontos)

        self.formLayout.addRow(QLabel(""), QLabel(""))

        self.label_ponto_inicial = QLabel("PONTO INICIAL:")

        self.x_ponto_inicial = QDoubleSpinBox()
        self.x_ponto_inicial.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.x_ponto_inicial.setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.y_ponto_inicial = QDoubleSpinBox()
        self.y_ponto_inicial.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.y_ponto_inicial.setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.formLayout.addRow(self.label_ponto_inicial, QLabel(""))
        self.formLayout.addRow(self.x_ponto_inicial, self.y_ponto_inicial)

        self.formLayout.addRow(QLabel(""), QLabel(""))

        self.label_primeiro_controle = QLabel("PRIMEIRO PONTO DE CONTROLE:")

        self.x_primeiro_controle = QDoubleSpinBox()
        self.x_primeiro_controle.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.x_primeiro_controle.setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.y_primeiro_controle = QDoubleSpinBox()
        self.y_primeiro_controle.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.y_primeiro_controle.setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.formLayout.addRow(self.label_primeiro_controle, QLabel(""))
        self.formLayout.addRow(self.x_primeiro_controle, self.y_primeiro_controle)

        self.formLayout.addRow(QLabel(""), QLabel(""))

        self.label_segundo_controle = QLabel("SEGUNDO PONTO DE CONTROLE:")

        self.x_segundo_controle = QDoubleSpinBox()
        self.x_segundo_controle.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.x_segundo_controle.setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.y_segundo_controle = QDoubleSpinBox()
        self.y_segundo_controle.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.y_segundo_controle.setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.formLayout.addRow(self.label_segundo_controle, QLabel(""))
        self.formLayout.addRow(self.x_segundo_controle, self.y_segundo_controle)

        self.formLayout.addRow(QLabel(""), QLabel(""))

        self.label_ponto_final = QLabel("PONTO FINAL:")

        self.x_ponto_final = QDoubleSpinBox()
        self.x_ponto_final.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.x_ponto_final.setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.y_ponto_final = QDoubleSpinBox()
        self.y_ponto_final.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.y_ponto_final.setMaximum(Config.valorMaximoQDoubleSpinBox())

        self.formLayout.addRow(self.label_ponto_final, QLabel(""))
        self.formLayout.addRow(self.x_ponto_final, self.y_ponto_final)

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

            self.dict_info["coordenadas"].append(
                (self.x_ponto_inicial.value(), self.y_ponto_inicial.value())
            )
            self.dict_info["coordenadas"].append(
                (self.x_primeiro_controle.value(), self.y_primeiro_controle.value())
            )
            self.dict_info["coordenadas"].append(
                (self.x_segundo_controle.value(), self.y_segundo_controle.value())
            )
            self.dict_info["coordenadas"].append(
                (self.x_ponto_final.value(), self.y_ponto_final.value())
            )

            self.dict_info["numero_de_pontos"] = self.spin_box_numero_pontos.value()

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
