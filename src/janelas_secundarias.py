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
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from config import Config


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
            "cor": (),
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
            self.dict_info["cor"] = (
                self.cor_R_objeto.value(),
                self.cor_G_objeto.value(),
                self.cor_B_objeto.value(),
            )
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


class transformacaoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.submitted = False
        self.transformacao = {"transformacao": "", "argumento": []}

        self.setWindowTitle("Transformações 2D")
        self.setMinimumSize(QtCore.QSize(500, 300))
        self.setMaximumSize(QtCore.QSize(500, 300))

        layout = QVBoxLayout()
        self.tab_widget = QTabWidget()

        # Instanciando as abas
        translacao = QWidget()
        rotacao = QWidget()
        escalonamento = QWidget()

        # Criando a aba da translacao
        translacao_label = QLabel("Escolha o ponto para a Translação")
        translacao_layout = QFormLayout()
        translacao_layout.setVerticalSpacing(20)  # Espacamento vertical entre as linhas
        translacao_layout.setHorizontalSpacing(10)  # Espacamento horizontal
        translacao_layout.addWidget(translacao_label)

        # Botao cancelar
        cancel_button_1 = QPushButton("Cancelar")
        cancel_button_1.clicked.connect(self.close)

        # Botao translacao
        translacao_button = QPushButton("OK")
        translacao_button.clicked.connect(self.translacao)

        # Coordenada x translacao
        self.translacao_x = QDoubleSpinBox()
        self.translacao_x.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.translacao_x.setMaximum(Config.valorMaximoQDoubleSpinBox())

        # Coordenada y translacao
        self.translacao_y = QDoubleSpinBox()
        self.translacao_y.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.translacao_y.setMaximum(Config.valorMaximoQDoubleSpinBox())

        # Layout translacao
        translacao_layout.addRow(QLabel("Desvio em X:"), self.translacao_x)
        translacao_layout.addRow(QLabel("Desvio em Y:"), self.translacao_y)
        translacao_layout.addRow(translacao_button, cancel_button_1)
        translacao.setLayout(translacao_layout)

        # Criando a aba da rotacao
        rotacao_label = QLabel("Escolha o ponto de Rotação")
        rotacao_layout = QFormLayout()
        rotacao_layout.setVerticalSpacing(20)  # Espacamento vertical entre as linhas
        rotacao_layout.setHorizontalSpacing(10)  # Espacamento horizontal
        rotacao_layout.addWidget(rotacao_label)

        # Botao cancelar
        cancel_button_2 = QPushButton("Cancelar")
        cancel_button_2.clicked.connect(self.close)

        # Botao rotacao
        rotacao_button = QPushButton("OK")
        rotacao_button.clicked.connect(self.rotacao)

        # Combo box rotacao
        self.rotacao_opcoes = QtWidgets.QComboBox()
        self.rotacao_opcoes.addItem("A Origem")
        self.rotacao_opcoes.addItem("Um Ponto")
        self.rotacao_opcoes.addItem("O Centro do Objeto")
        rotacao_layout.addWidget(self.rotacao_opcoes)

        # Angulo da rotacao
        self.rotacao_angulo = QDoubleSpinBox()
        self.rotacao_angulo.setMinimum(0)
        self.rotacao_angulo.setMaximum(360)

        # Coordenada x rotacao
        self.rotacao_x = QDoubleSpinBox()
        self.rotacao_x.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.rotacao_x.setMaximum(Config.valorMaximoQDoubleSpinBox())

        # Coordenada y rotacao
        self.rotacao_y = QDoubleSpinBox()
        self.rotacao_y.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.rotacao_y.setMaximum(Config.valorMaximoQDoubleSpinBox())

        # Layout rotacao
        rotacao_layout.addRow(QLabel("Coordenada X do ponto: "), self.rotacao_x)
        rotacao_layout.addRow(QLabel("Coordenada Y do ponto: "), self.rotacao_y)
        rotacao_layout.addRow(QLabel("Ângulo da Rotação: "), self.rotacao_angulo)

        rotacao_layout.addRow(rotacao_button, cancel_button_2)
        rotacao.setLayout(rotacao_layout)

        # Criando a aba do escalonamento
        escalonamento_label = QLabel("Escolha a escala para o Escalonamento")
        escalonamento_layout = QFormLayout()
        escalonamento_layout.setVerticalSpacing(
            20
        )  # Espacamento vertical entre as linhas
        escalonamento_layout.setHorizontalSpacing(10)  # Espacamento horizontal
        escalonamento_layout.addWidget(escalonamento_label)

        # Botao cancelar
        cancel_button_3 = QPushButton("Cancelar")
        cancel_button_3.clicked.connect(self.close)

        # Botao escalonamento
        escalonamento_button = QPushButton("OK")
        escalonamento_button.clicked.connect(self.escalonamento)

        # Valor do escalonamento
        self.escalonamento_valor = QDoubleSpinBox()
        self.escalonamento_valor.setMinimum(Config.valorMinimoQDoubleSpinBox())
        self.escalonamento_valor.setMaximum(Config.valorMaximoQDoubleSpinBox())

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
            (self.translacao_x.value(), self.translacao_y.value())
        )
        self.accept()

    def rotacao(self):
        self.transformacao["transformacao"] = "rotacao"
        self.transformacao["argumento"].append(self.rotacao_angulo.value())
        if self.rotacao_opcoes.currentIndex() == 0:
            self.transformacao["argumento"].append((None, "origem"))
        elif self.rotacao_opcoes.currentIndex() == 1:
            self.transformacao["argumento"].append(
                (self.rotacao_x.value(), self.rotacao_y.value())
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

        x = pedirNome.exec_()


class recolorirDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.submitted = False

        self.setWindowTitle("Recolorir Objeto")
        self.formLayout = QFormLayout()

        self.setMinimumSize(QtCore.QSize(275, 150))
        self.setMaximumSize(QtCore.QSize(275, 150))

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

        button_ok = QPushButton("OK")
        button_cancel = QPushButton("Cancelar")

        button_ok.clicked.connect(self.accept)
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


class numero_pontosDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.submitted = False

        self.setWindowTitle("Criar Objeto")
        layout = QVBoxLayout()

        self.setMinimumSize(QtCore.QSize(300, 150))
        self.setMaximumSize(QtCore.QSize(300, 150))

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
