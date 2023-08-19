# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototipo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from janelas_secundarias import AdicionarDialog, OperacoesDialog

class Ui_MainDisplay(object):
    def setupUi(self, MainDisplay):
        MainDisplay.setObjectName("MainDisplay")
        MainDisplay.resize(960, 540)
        MainDisplay.setMinimumSize(QtCore.QSize(960, 540))
        MainDisplay.setMaximumSize(QtCore.QSize(960, 540))
        MainDisplay.setStyleSheet("background-color: rgb(212,208,200);")
        self.centralwidget = QtWidgets.QWidget(MainDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_viewport = QtWidgets.QFrame(self.centralwidget)
        self.frame_viewport.setStyleSheet("background-color: rgb(212, 208, 200);\n"
"")
        self.frame_viewport.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_viewport.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_viewport.setObjectName("frame_viewport")
        self.frame_movimentacao_window = QtWidgets.QFrame(self.frame_viewport)
        self.frame_movimentacao_window.setGeometry(QtCore.QRect(480, 220, 431, 281))
        self.frame_movimentacao_window.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_movimentacao_window.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_movimentacao_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_movimentacao_window.setObjectName("frame_movimentacao_window")
        self.line_minimo_x = QtWidgets.QLineEdit(self.frame_movimentacao_window)
        self.line_minimo_x.setGeometry(QtCore.QRect(260, 90, 71, 31))
        self.line_minimo_x.setObjectName("line_minimo_x")
        self.line_maximo_x = QtWidgets.QLineEdit(self.frame_movimentacao_window)
        self.line_maximo_x.setGeometry(QtCore.QRect(340, 90, 71, 31))
        self.line_maximo_x.setObjectName("line_maximo_x")
        self.line_minimo_y = QtWidgets.QLineEdit(self.frame_movimentacao_window)
        self.line_minimo_y.setGeometry(QtCore.QRect(260, 130, 71, 31))
        self.line_minimo_y.setObjectName("line_minimo_y")
        self.line_maximo_y = QtWidgets.QLineEdit(self.frame_movimentacao_window)
        self.line_maximo_y.setGeometry(QtCore.QRect(340, 130, 71, 31))
        self.line_maximo_y.setObjectName("line_maximo_y")
        self.texto_x = QtWidgets.QTextBrowser(self.frame_movimentacao_window)
        self.texto_x.setGeometry(QtCore.QRect(230, 90, 31, 21))
        self.texto_x.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_x.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_x.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_x.setObjectName("texto_x")
        self.texto_y = QtWidgets.QTextBrowser(self.frame_movimentacao_window)
        self.texto_y.setGeometry(QtCore.QRect(230, 130, 31, 21))
        self.texto_y.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_y.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_y.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_y.setObjectName("texto_y")
        self.texto_minimo = QtWidgets.QTextBrowser(self.frame_movimentacao_window)
        self.texto_minimo.setGeometry(QtCore.QRect(260, 60, 71, 21))
        self.texto_minimo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_minimo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_minimo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_minimo.setObjectName("texto_minimo")
        self.texto_maximo = QtWidgets.QTextBrowser(self.frame_movimentacao_window)
        self.texto_maximo.setGeometry(QtCore.QRect(340, 60, 71, 21))
        self.texto_maximo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_maximo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_maximo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_maximo.setObjectName("texto_maximo")
        self.texto_coordenadas = QtWidgets.QTextBrowser(self.frame_movimentacao_window)
        self.texto_coordenadas.setGeometry(QtCore.QRect(260, 20, 151, 21))
        self.texto_coordenadas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_coordenadas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_coordenadas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_coordenadas.setObjectName("texto_coordenadas")
        self.up_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.up_button.setGeometry(QtCore.QRect(80, 120, 61, 28))
        self.up_button.setAutoDefault(False)
        self.up_button.setDefault(False)
        self.up_button.setFlat(False)
        self.up_button.setObjectName("up_button")
        self.down_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.down_button.setGeometry(QtCore.QRect(80, 240, 61, 28))
        self.down_button.setObjectName("down_button")
        self.right_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.right_button.setGeometry(QtCore.QRect(140, 180, 61, 28))
        self.right_button.setObjectName("right_button")
        self.left_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.left_button.setGeometry(QtCore.QRect(20, 180, 61, 28))
        self.left_button.setFlat(False)
        self.left_button.setObjectName("left_button")
        self.zoom_in_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.zoom_in_button.setGeometry(QtCore.QRect(20, 40, 61, 28))
        self.zoom_in_button.setObjectName("zoom_in_button")
        self.zoom_out_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.zoom_out_button.setGeometry(QtCore.QRect(140, 40, 61, 28))
        self.zoom_out_button.setObjectName("zoom_out_button")
        self.texto_precisao = QtWidgets.QTextBrowser(self.frame_movimentacao_window)
        self.texto_precisao.setGeometry(QtCore.QRect(290, 190, 71, 21))
        self.texto_precisao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_precisao.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_precisao.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_precisao.setObjectName("texto_precisao")
        self.line_precisao = QtWidgets.QLineEdit(self.frame_movimentacao_window)
        self.line_precisao.setGeometry(QtCore.QRect(290, 220, 71, 31))
        self.line_precisao.setObjectName("line_precisao")
        self.viewport = QtWidgets.QFrame(self.frame_viewport)
        self.viewport.setGeometry(QtCore.QRect(10, 40, 451, 461))
        self.viewport.setMaximumSize(QtCore.QSize(500, 16777215))
        self.viewport.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"")
        self.viewport.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.viewport.setFrameShadow(QtWidgets.QFrame.Raised)
        self.viewport.setObjectName("viewport")
        self.texto_controle_window = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_controle_window.setGeometry(QtCore.QRect(480, 190, 151, 21))
        self.texto_controle_window.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_controle_window.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_controle_window.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_controle_window.setObjectName("texto_controle_window")
        self.ListaDeObjetos = QtWidgets.QComboBox(self.frame_viewport)
        self.ListaDeObjetos.setGeometry(QtCore.QRect(750, 50, 151, 31))
        self.ListaDeObjetos.setObjectName("ListaDeObjetos")
        self.ListaDeObjetos.addItem("")
        self.ListaDeObjetos.addItem("")
        self.ListaDeObjetos.addItem("")
        self.ListaDeObjetos.addItem("")
        self.ListaDeObjetos.addItem("")
        self.AdicionarObjetos = QtWidgets.QComboBox(self.frame_viewport)
        self.AdicionarObjetos.setGeometry(QtCore.QRect(500, 50, 151, 31))
        self.AdicionarObjetos.setObjectName("AdicionarObjetos")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")
        self.texto_adicionar_objeto = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_adicionar_objeto.setGeometry(QtCore.QRect(480, 20, 151, 21))
        self.texto_adicionar_objeto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_adicionar_objeto.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_adicionar_objeto.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_adicionar_objeto.setObjectName("texto_adicionar_objeto")
        self.texto_lista_objetos = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_lista_objetos.setGeometry(QtCore.QRect(730, 20, 151, 21))
        self.texto_lista_objetos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_lista_objetos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_lista_objetos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_lista_objetos.setObjectName("texto_lista_objetos")
        self.texto_viewport = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_viewport.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.texto_viewport.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_viewport.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_viewport.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texto_viewport.setObjectName("texto_viewport")
        self.adicionar_button = QtWidgets.QPushButton(self.frame_viewport)
        self.adicionar_button.setGeometry(QtCore.QRect(530, 90, 75, 23))
        self.adicionar_button.setObjectName("adicionar_button")
        self.operacoes_button = QtWidgets.QPushButton(self.frame_viewport)
        self.operacoes_button.setGeometry(QtCore.QRect(780, 90, 75, 23))
        self.operacoes_button.setObjectName("operacoes_button")
        self.verticalLayout.addWidget(self.frame_viewport)
        MainDisplay.setCentralWidget(self.centralwidget)

        #Configurando os botoes
        self.adicionar_button.clicked.connect(self.pop_up_digitar_pontos)
        self.operacoes_button.clicked.connect(self.pop_up_realizar_operacao)


        self.retranslateUi(MainDisplay)
        QtCore.QMetaObject.connectSlotsByName(MainDisplay)

    def retranslateUi(self, MainDisplay):
        _translate = QtCore.QCoreApplication.translate
        MainDisplay.setWindowTitle(_translate("MainDisplay", "Graphic Application"))
        self.texto_x.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X</p></body></html>"))
        self.texto_y.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Y</p></body></html>"))
        self.texto_minimo.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mínimo</p></body></html>"))
        self.texto_maximo.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Máximo</p></body></html>"))
        self.texto_coordenadas.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Coordenadas</span></p></body></html>"))
        self.up_button.setText(_translate("MainDisplay", "▲"))
        self.down_button.setText(_translate("MainDisplay", "▼"))
        self.right_button.setText(_translate("MainDisplay", "►"))
        self.left_button.setText(_translate("MainDisplay", "◄"))
        self.zoom_in_button.setText(_translate("MainDisplay", "Zoom In"))
        self.zoom_out_button.setText(_translate("MainDisplay", "Zoom Out"))
        self.texto_precisao.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Precisão</span></p></body></html>"))
        self.texto_controle_window.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Controle da Window</p></body></html>"))
        self.ListaDeObjetos.setItemText(0, _translate("MainDisplay", "Nenhum"))
        self.ListaDeObjetos.setItemText(1, _translate("MainDisplay", "Ponto"))
        self.ListaDeObjetos.setItemText(2, _translate("MainDisplay", "Reta"))
        self.ListaDeObjetos.setItemText(3, _translate("MainDisplay", "Wireframe"))
        self.ListaDeObjetos.setItemText(4, _translate("MainDisplay", "Curva"))
        self.AdicionarObjetos.setItemText(0, _translate("MainDisplay", "Ponto"))
        self.AdicionarObjetos.setItemText(1, _translate("MainDisplay", "Reta"))
        self.AdicionarObjetos.setItemText(2, _translate("MainDisplay", "Wireframe"))
        self.AdicionarObjetos.setItemText(3, _translate("MainDisplay", "Curva"))
        self.texto_adicionar_objeto.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adicionar Objeto</p></body></html>"))
        self.texto_lista_objetos.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lista de Objetos</p></body></html>"))
        self.texto_viewport.setHtml(_translate("MainDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Viewport</p></body></html>"))
        self.adicionar_button.setText(_translate("MainDisplay", "Adicionar"))
        self.operacoes_button.setText(_translate("MainDisplay", "Operações"))

    def pop_up_digitar_pontos(self):
            if (self.AdicionarObjetos.currentText() == "Wireframe"):
                    #TODO: Abre um QMessageBox perguntando quantos pontos tem o poligono
                    pass

            getCoordenadas = AdicionarDialog()
            #getCoordenadas.move() Fazer com que o QDialog abra no centro da nossa aplicacao

            print(self.AdicionarObjetos.currentText())


            x = getCoordenadas.exec_()

    def pop_up_realizar_operacao(self):
            fazOperacao = QMessageBox()
            fazOperacao.setWindowTitle("Escolha a operacao a ser feita!")
            fazOperacao.setText("Aqui estarao rotacao, delete entre outros ('_>')")

            x = fazOperacao.exec_()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainDisplay = QtWidgets.QMainWindow()
        ui = Ui_MainDisplay()
        ui.setupUi(MainDisplay)
        MainDisplay.show()
        sys.exit(app.exec_())
