from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtWidgets, QtCore

class AdicionarDialog(QDialog):
    def __init__(self):
        super().__init__()
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


        #Scroll bar
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 351, 241))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        #nao sei oq fazem ainda
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 349, 239))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.standard_buttons.accepted.connect(self.accept)  # type: ignore
        self.standard_buttons.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)


    #def accept(self):     É possivel sobreescrever os métodos dos botoes --> Importante para coletar os dados dps
        #print("Ai minha voaida")






class OperacoesDialog(QDialog):
    def __init__(self):
        super().__init__()
        pass