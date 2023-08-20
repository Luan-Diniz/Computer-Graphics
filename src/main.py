import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPainter, QPen
from PyQt5.QtWidgets import QMessageBox

from config import Config
from display_file import DisplayFile
from janelas_secundarias import *
from shapes import Ponto, Reta, Wireframe
from window import Window


class Ui_MainDisplay(object):
    def setupUi(self, MainDisplay):
        MainDisplay.setObjectName("MainDisplay")
        MainDisplay.resize(960, 540)
        MainDisplay.setMinimumSize(QtCore.QSize(960, 540))
        MainDisplay.setMaximumSize(QtCore.QSize(960, 540))
        MainDisplay.setStyleSheet("background-color: rgb(212,208,200);")

        # instanciando classes
        self.window = Window()
        self.display_file = (
            DisplayFile()
        )  # no display file os elementos graficos ficarao guardados

        self.centralwidget = QtWidgets.QWidget(MainDisplay)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_viewport = QtWidgets.QFrame(self.centralwidget)
        self.frame_viewport.setStyleSheet("background-color: rgb(212, 208, 200);\n" "")
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
        self.texto_coordenadas.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
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
        self.viewport.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-width : 1.2px;\n"
            "border-style:inset;\n"
            ""
        )
        self.viewport.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.viewport.setFrameShadow(QtWidgets.QFrame.Raised)
        self.viewport.setObjectName("viewport")

        # Criando uma Label para o desenho dos Objetos
        self.area_desenho = QtWidgets.QLabel("", self.frame_viewport)
        canvas = QtGui.QPixmap(451, 461)
        canvas.fill(Qt.white)
        self.area_desenho.setPixmap(canvas)
        self.area_desenho.setGeometry(QtCore.QRect(10, 40, 451, 461))

        self.texto_controle_window = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_controle_window.setGeometry(QtCore.QRect(480, 190, 151, 21))
        self.texto_controle_window.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_controle_window.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_controle_window.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_controle_window.setObjectName("texto_controle_window")

        self.ListaDeObjetos = QtWidgets.QComboBox(self.frame_viewport)
        self.ListaDeObjetos.setGeometry(QtCore.QRect(750, 50, 151, 31))
        self.ListaDeObjetos.setObjectName("ListaDeObjetos")

        self.AdicionarObjetos = QtWidgets.QComboBox(self.frame_viewport)
        self.AdicionarObjetos.setGeometry(QtCore.QRect(500, 50, 151, 31))
        self.AdicionarObjetos.setObjectName("AdicionarObjetos")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")

        self.texto_adicionar_objeto = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_adicionar_objeto.setGeometry(QtCore.QRect(480, 20, 151, 21))
        self.texto_adicionar_objeto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_adicionar_objeto.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_adicionar_objeto.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_adicionar_objeto.setObjectName("texto_adicionar_objeto")

        self.texto_lista_objetos = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_lista_objetos.setGeometry(QtCore.QRect(730, 20, 151, 21))
        self.texto_lista_objetos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_lista_objetos.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_lista_objetos.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
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

        # Configurando os botoes
        self.adicionar_button.clicked.connect(self.pop_up_digitar_pontos)
        self.operacoes_button.clicked.connect(self.pop_up_realizar_operacao)
        self.right_button.clicked.connect(self.move_direita)
        self.left_button.clicked.connect(self.move_esquerda)
        self.up_button.clicked.connect(self.move_cima)
        self.down_button.clicked.connect(self.move_baixo)
        self.zoom_in_button.clicked.connect(self.ZoomIn)
        self.zoom_out_button.clicked.connect(self.ZoomOut)

        self.retranslateUi(MainDisplay)
        QtCore.QMetaObject.connectSlotsByName(MainDisplay)

    def retranslateUi(self, MainDisplay):
        _translate = QtCore.QCoreApplication.translate
        MainDisplay.setWindowTitle(_translate("MainDisplay", "Sistema Gráfico 2D"))
        self.texto_x.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">X</p></body></html>',
            )
        )
        self.texto_y.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Y</p></body></html>',
            )
        )
        self.texto_minimo.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Mínimo</p></body></html>',
            )
        )
        self.texto_maximo.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Máximo</p></body></html>',
            )
        )
        self.texto_coordenadas.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Coordenadas</span></p></body></html>',
            )
        )
        self.up_button.setText(_translate("MainDisplay", "▲"))
        self.down_button.setText(_translate("MainDisplay", "▼"))
        self.right_button.setText(_translate("MainDisplay", "►"))
        self.left_button.setText(_translate("MainDisplay", "◄"))
        self.zoom_in_button.setText(_translate("MainDisplay", "Zoom In"))
        self.zoom_out_button.setText(_translate("MainDisplay", "Zoom Out"))
        self.texto_precisao.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Precisão</span></p></body></html>',
            )
        )
        self.texto_controle_window.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Controle da Window</p></body></html>',
            )
        )
        self.AdicionarObjetos.setItemText(0, _translate("MainDisplay", "Ponto"))
        self.AdicionarObjetos.setItemText(1, _translate("MainDisplay", "Reta"))
        self.AdicionarObjetos.setItemText(2, _translate("MainDisplay", "Wireframe"))
        self.texto_adicionar_objeto.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Adicionar Objeto</p></body></html>',
            )
        )
        self.texto_lista_objetos.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Lista de Objetos</p></body></html>',
            )
        )
        self.texto_viewport.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Viewport</p></body></html>',
            )
        )
        self.adicionar_button.setText(_translate("MainDisplay", "Adicionar"))
        self.operacoes_button.setText(_translate("MainDisplay", "Operações"))

    def quantidade_de_pontos(self):
        qtdPontos = numero_pontosDialog()
        x = qtdPontos.exec_()

        print(qtdPontos.submitted)
        if qtdPontos.submitted:
            return qtdPontos.numero_pontos()
        return -1

    def pop_up_digitar_pontos(self):
        error = False

        if self.AdicionarObjetos.currentText() == "Wireframe":
            # TODO: Abre um QMessageBox/QDialog perguntando quantos pontos tem o poligono
            qtd_pontos = self.quantidade_de_pontos()

            if qtd_pontos != -1:
                getCoordenadas = AdicionarDialog(
                    qtd_pontos, self.display_file.getNomesElementosGraficos()
                )
            else:
                error = True

        elif self.AdicionarObjetos.currentText() == "Ponto":
            getCoordenadas = AdicionarDialog(
                1, self.display_file.getNomesElementosGraficos()
            )
        elif self.AdicionarObjetos.currentText() == "Reta":
            getCoordenadas = AdicionarDialog(
                2, self.display_file.getNomesElementosGraficos()
            )

        if not error:
            x = getCoordenadas.exec_()
            # Aqui roda após "fechar a janela, mas ainda é possível acessar seus atributos"
            if getCoordenadas.submitted:
                if self.AdicionarObjetos.currentText() == "Ponto":
                    elemento_grafico = Ponto(
                        getCoordenadas.dict_info["nome"],
                        getCoordenadas.dict_info["coordenadas"],
                    )
                    self.drawPoint(elemento_grafico)
                elif self.AdicionarObjetos.currentText() == "Reta":
                    elemento_grafico = Reta(
                        getCoordenadas.dict_info["nome"],
                        getCoordenadas.dict_info["coordenadas"],
                    )
                    self.drawLine(elemento_grafico)
                else:
                    elemento_grafico = Wireframe(
                        getCoordenadas.dict_info["nome"],
                        getCoordenadas.dict_info["coordenadas"],
                    )
                    self.drawWireframe(elemento_grafico)

                self.display_file.adicionar(elemento_grafico)

                # Adicionando objeto criado na lista de objetos
                self.ListaDeObjetos.addItem(getCoordenadas.dict_info["nome"])

    def pop_up_realizar_operacao(self):
        fazOperacao = QMessageBox()
        fazOperacao.setWindowTitle("Operações")
        fazOperacao.setText("Escolha a operacao a ser feita")

        # Criando os botoes
        fazOperacao.setStandardButtons(QMessageBox.Abort)
        botao_deletar = fazOperacao.button(QMessageBox.Abort)
        botao_deletar.setText("Deletar Objeto")

        # Chamando o metodo de cada botao
        fazOperacao.buttonClicked.connect(self.definir_operacao)

        x = fazOperacao.exec_()

    def definir_operacao(self, i):
        if i.text() == "Deletar Objeto":
            self.deletar_objeto()

    def deletar_objeto(self):
        # Deleta o objeto selecionado
        if self.ListaDeObjetos.count() > 0:
            i = self.ListaDeObjetos.currentIndex()
            self.ListaDeObjetos.removeItem(i)
            elemento_grafico = self.display_file.getElementoGrafico(i)
            self.display_file.remover(i)
            self.eraseDraw(elemento_grafico)

    def drawObj(self, elemento_grafico):
        if elemento_grafico.get_tipo() == "Ponto":
            self.drawPoint(elemento_grafico)
        elif elemento_grafico.get_tipo() == "Reta":
            self.drawLine(elemento_grafico)
        else:
            self.drawWireframe(elemento_grafico)

    def eraseDraw(self, elemento_grafico):
        canvas = QtGui.QPixmap(451, 461)
        canvas.fill(Qt.white)
        self.area_desenho.setPixmap(canvas)

        for obj in self.display_file.getListaElementosGraficos():
            self.drawObj(obj)

    def drawPoint(self, ponto: Ponto):
        painter = QtGui.QPainter(self.area_desenho.pixmap())

        # Definindo car e tamanho do ponto
        pen = QPen(Qt.red, 5)
        painter.setPen(pen)

        # Desenhando o ponto
        painter.drawPoint(
            int(ponto.get_coordenadas()[0][0]), int(ponto.get_coordenadas()[0][1])
        )
        painter.end()
        print("Ponto adicionado!")

    def drawLine(self, reta: Reta):
        pontos = reta.get_coordenadas()
        painter = QtGui.QPainter(self.area_desenho.pixmap())

        # Definindo a cor e tamanho da reta
        pen = QPen(Qt.blue, 5)
        painter.setPen(pen)

        # Desenhando a reta
        painter.drawLine(
            int(pontos[0][0]), int(pontos[0][1]), int(pontos[1][0]), int(pontos[1][1])
        )
        painter.end()
        print("Reta adicionada!")

    def drawWireframe(self, wireframe: Wireframe):
        pontos = wireframe.get_coordenadas()
        painter = QtGui.QPainter(self.area_desenho.pixmap())
        pen = QPen(Qt.black, 5)
        painter.setPen(pen)

        for i in range(len(pontos)):
            if i != len(pontos) - 1:
                painter.drawLine(
                    int(pontos[i][0]),
                    int(pontos[i][1]),
                    int(pontos[i + 1][0]),
                    int(pontos[i + 1][1]),
                )
            else:
                painter.drawLine(
                    int(pontos[i][0]),
                    int(pontos[i][1]),
                    int(pontos[0][0]),
                    int(pontos[0][1]),
                )

        painter.end()
        print("Wireframe adicionado!")

    def move_direita(self):
        self.window.moveuDireita()
        # TODO: Funcao para resenhar o viewport

    def move_esquerda(self):
        self.window.moveuEsquerda()
        # TODO: Funcao para resenhar o viewport

    def move_cima(self):
        self.window.moveuCima()
        # TODO: Funcao para resenhar o viewport

    def move_baixo(self):
        self.window.moveuBaixo()
        # TODO: Funcao para resenhar o viewport

    def ZoomIn(self):
        self.window.ZoomIn()
        # TODO: Funcao para resenhar o viewport

    def ZoomOut(self):
        self.window.ZoomOut()
        # TODO: Funcao para resenhar o viewport


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainDisplay = QtWidgets.QMainWindow()
    ui = Ui_MainDisplay()
    ui.setupUi(MainDisplay)
    MainDisplay.show()
    sys.exit(app.exec_())
