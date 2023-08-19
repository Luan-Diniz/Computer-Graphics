from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QWidget, QFormLayout, QGroupBox
from PyQt5 import QtWidgets, QtCore

class AdicionarDialog(QDialog):
    def __init__(self,qtdade_coordenadas):
        super().__init__()
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

        self.labelList = []
        self.buttonList = []

        #MELHORAR ESSE FOR!!!!!
        for i in range(0, self.qtdade_coordenadas):
            self.labelList.append(QLabel(f"X{i + 1}"))
            self.buttonList.append(QPushButton(f"Do not "))
            self.formLayout.addRow(self.labelList[i], self.buttonList[i])

            self.labelList.append(QLabel(f"Y{i + 1}"))
            self.buttonList.append(QPushButton(f"Do not "))
            self.formLayout.addRow(self.labelList[i], self.buttonList[i])

        self.groupBox.setLayout(self.formLayout)



        #Scroll bar
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 351, 241))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        #nao sei oq fazem ainda
        self.scrollArea.setObjectName("scrollArea")
        #self.scrollAreaWidgetContents = QtWidgets.QWidget()
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 349, 239))
        #self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.groupBox)
        self.scrollArea.setWidgetResizable(True)

        self.standard_buttons.accepted.connect(self.accept)  # type: ignore
        self.standard_buttons.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)


    #usar QDoubleSpinBox para o usuário digitar os floats


    #def accept(self):     É possivel sobreescrever os métodos dos botoes --> Importante para coletar os dados dps
        #print("Ai minha voaida")






class OperacoesDialog(QDialog):
    def __init__(self):
        super().__init__()
        pass