from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QWidget, QFormLayout, QGroupBox, QDoubleSpinBox, QLineEdit, QMessageBox
from PyQt5 import QtWidgets, QtCore

class AdicionarDialog(QDialog):
    def __init__(self,qtdade_coordenadas):
        super().__init__()

        #Só será True se o usuário clicar em ok (a funcao accept torna ele True)
        self.submitted = False
        #Nesse dicionario será armazenado as informações do objeto que sera criado
        self.dict_info = {
            "nome": "",
            "coordenadas": [],
        }

        self.qtdade_coordenadas = qtdade_coordenadas
        self.setWindowTitle("Digite as coordenadas!")

        self.resize(400, 300)
        self.setMinimumSize(QtCore.QSize(400, 300))
        self.setMaximumSize(QtCore.QSize(400, 300))
        self.setStyleSheet("background-color: rgb(165, 165, 165);")
        self.standard_buttons = QtWidgets.QDialogButtonBox(self)
        self.standard_buttons.setGeometry(QtCore.QRect(50, 260, 341, 32))
        self.standard_buttons.setStyleSheet("background-color: rgb(212,208,200);")
        self.standard_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.standard_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.standard_buttons.setObjectName("standard_buttons")


        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox()

        self.labelXList = []
        self.labelYList = []
        self.coordinateXList = []
        self.coordinateYList = []

        #Cria o label e a entrada para um nome.
        self.labelNome = QLabel("Nome: ")
        self.nome_objeto = QLineEdit()
        self.formLayout.addRow(self.labelNome, self.nome_objeto)

        #Cria os QDoubleSpinBox para entrada numérica.
        for i in range(0, self.qtdade_coordenadas):
            self.labelXList.append(QLabel(f"X{i + 1}"))
            self.coordinateXList.append(QDoubleSpinBox())
            self.labelYList.append(QLabel(f"Y{i + 1}"))
            self.coordinateYList.append(QDoubleSpinBox())
            self.formLayout.addRow(self.labelXList[i], self.coordinateXList[i])
            self.formLayout.addRow(self.labelYList[i], self.coordinateYList[i])



        self.groupBox.setLayout(self.formLayout)



        #Scroll bar
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 351, 241))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidget(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.standard_buttons.accepted.connect(self.accept)  # type: ignore
        self.standard_buttons.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)



    def accept(self):     #Sobreescrita do metodo do botao accept
        #TODO: Verificar se os dados estao inseridos corretamente
        #(tem que ter nome) --> se n tiver abre um QMessageBox avisando o erro

        nome = self.nome_objeto.text()

        if(len(nome.replace(" ", "")) == 0):
            #self.pedir_nome()
            pass

        self.dict_info["nome"] = nome
        for i in range(0, self.qtdade_coordenadas):
            self.dict_info["coordenadas"].append((self.coordinateXList[i].value(), self.coordinateYList[i].value()))

        self.submitted = True
        self.close()  #Fecha a window

    def pedir_nome(self):
        pedirNome = QMessageBox()
        pedirNome.setWindowTitle("Aviso!")
        pedirNome.setIcon(QMessageBox.Critical)
        pedirNome.setText("O objeto precisa ter um nome!")

        x = pedirNome.exec_()





class OperacoesDialog(QDialog):
    def __init__(self):
        super().__init__()
        pass