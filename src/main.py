import sys
from math import cos, radians, sin
from os.path import exists, splitext

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from descritorobj import GeradorOBJ, LeitorOBJ
from display_file import DisplayFile
from formulas_matematicas import FormulasMatematicas
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

        # Instanciando as classes
        self.window = Window()
        self.display_file = (
            DisplayFile()
        )  # Os elementos graficos ficarao guardados no Display File

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
        self.frame_movimentacao_window.setGeometry(QtCore.QRect(480, 350, 435, 150))
        self.frame_movimentacao_window.setStyleSheet(
            "background-color: rgb(165,165,165);"
        )
        self.frame_movimentacao_window.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_movimentacao_window.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_movimentacao_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_movimentacao_window.setObjectName("frame_movimentacao_window")

        self.frame_gerenciar_arquivos = QtWidgets.QFrame(self.frame_viewport)
        self.frame_gerenciar_arquivos.setGeometry(QtCore.QRect(480, 205, 435, 110))
        self.frame_gerenciar_arquivos.setStyleSheet(
            "background-color: rgb(165,165,165);"
        )
        self.frame_gerenciar_arquivos.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_gerenciar_arquivos.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_gerenciar_arquivos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gerenciar_arquivos.setObjectName("frame_gerenciar_arquivos")

        self.frame_gerenciar_objetos = QtWidgets.QFrame(self.frame_viewport)
        self.frame_gerenciar_objetos.setGeometry(QtCore.QRect(480, 55, 435, 120))
        self.frame_gerenciar_objetos.setStyleSheet(
            "background-color: rgb(165,165,165);"
        )
        self.frame_gerenciar_objetos.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_gerenciar_objetos.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_gerenciar_objetos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gerenciar_objetos.setObjectName("frame_gerenciar_objetos")

        self.up_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.up_button.setGeometry(QtCore.QRect(80, 10, 60, 30))
        self.up_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.up_button.setAutoDefault(False)
        self.up_button.setDefault(False)
        self.up_button.setFlat(False)
        self.up_button.setObjectName("up_button")

        self.down_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.down_button.setGeometry(QtCore.QRect(80, 110, 60, 30))
        self.down_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.down_button.setObjectName("down_button")

        self.right_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.right_button.setGeometry(QtCore.QRect(140, 60, 60, 30))
        self.right_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.right_button.setObjectName("right_button")

        self.left_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.left_button.setGeometry(QtCore.QRect(20, 60, 60, 30))
        self.left_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.left_button.setFlat(False)
        self.left_button.setObjectName("left_button")

        self.zoom_in_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.zoom_in_button.setGeometry(QtCore.QRect(250, 30, 60, 30))
        self.zoom_in_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.zoom_in_button.setObjectName("zoom_in_button")

        self.zoom_out_button = QtWidgets.QPushButton(self.frame_movimentacao_window)
        self.zoom_out_button.setGeometry(QtCore.QRect(250, 90, 60, 30))
        self.zoom_out_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.zoom_out_button.setObjectName("zoom_out_button")

        self.anticlockwise_rotation_button = QtWidgets.QPushButton(
            self.frame_movimentacao_window
        )
        self.anticlockwise_rotation_button.setGeometry(QtCore.QRect(355, 30, 60, 30))
        self.anticlockwise_rotation_button.setStyleSheet(
            "background-color: rgb(212, 208, 200);"
        )
        self.anticlockwise_rotation_button.setObjectName(
            "anticlockwise_rotation_button"
        )

        self.clockwise_rotation_button = QtWidgets.QPushButton(
            self.frame_movimentacao_window
        )
        self.clockwise_rotation_button.setGeometry(QtCore.QRect(355, 90, 60, 30))
        self.clockwise_rotation_button.setStyleSheet(
            "background-color: rgb(212, 208, 200);"
        )
        self.clockwise_rotation_button.setObjectName("clockwise_rotation_button")

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
        self.texto_controle_window.setGeometry(QtCore.QRect(620, 325, 151, 21))
        self.texto_controle_window.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_controle_window.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_controle_window.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_controle_window.setObjectName("texto_controle_window")

        self.texto_gerenciar_arquivos = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_gerenciar_arquivos.setGeometry(QtCore.QRect(620, 180, 151, 21))
        self.texto_gerenciar_arquivos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_gerenciar_arquivos.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_gerenciar_arquivos.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_gerenciar_arquivos.setObjectName("texto_gerenciar_arquivos")

        self.texto_gerenciar_objetos = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_gerenciar_objetos.setGeometry(QtCore.QRect(620, 30, 151, 21))
        self.texto_gerenciar_objetos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_gerenciar_objetos.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_gerenciar_objetos.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_gerenciar_objetos.setObjectName("texto_gerenciar_objetos")

        self.ListaDeObjetos = QtWidgets.QComboBox(self.frame_viewport)
        self.ListaDeObjetos.setGeometry(QtCore.QRect(750, 90, 150, 30))
        self.ListaDeObjetos.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.ListaDeObjetos.setObjectName("ListaDeObjetos")

        self.AdicionarObjetos = QtWidgets.QComboBox(self.frame_viewport)
        self.AdicionarObjetos.setGeometry(QtCore.QRect(500, 90, 150, 30))
        self.AdicionarObjetos.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.AdicionarObjetos.setObjectName("AdicionarObjetos")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")

        self.texto_adicionar_objeto = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_adicionar_objeto.setGeometry(QtCore.QRect(490, 60, 120, 21))
        self.texto_adicionar_objeto.setStyleSheet("background-color: rgb(165,165,165);")
        self.texto_adicionar_objeto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texto_adicionar_objeto.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_adicionar_objeto.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.texto_adicionar_objeto.setObjectName("texto_adicionar_objeto")

        self.texto_lista_objetos = QtWidgets.QTextBrowser(self.frame_viewport)
        self.texto_lista_objetos.setGeometry(QtCore.QRect(740, 60, 120, 21))
        self.texto_lista_objetos.setStyleSheet("background-color: rgb(165,165,165);")
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
        self.adicionar_button.setGeometry(QtCore.QRect(530, 135, 75, 30))
        self.adicionar_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.adicionar_button.setObjectName("adicionar_button")

        self.operacoes_button = QtWidgets.QPushButton(self.frame_viewport)
        self.operacoes_button.setGeometry(QtCore.QRect(780, 135, 75, 30))
        self.operacoes_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.operacoes_button.setObjectName("operacoes_button")

        self.ler_arquivo_button = QtWidgets.QPushButton(self.frame_viewport)
        self.ler_arquivo_button.setGeometry(QtCore.QRect(535, 270, 75, 30))
        self.ler_arquivo_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.ler_arquivo_button.setObjectName("ler_arquivo_button")

        self.gerar_arquivo_button = QtWidgets.QPushButton(self.frame_viewport)
        self.gerar_arquivo_button.setGeometry(QtCore.QRect(780, 270, 75, 30))
        self.gerar_arquivo_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.gerar_arquivo_button.setObjectName("gerar_arquivo_button")

        self.nome_arquivo_entrada = QLineEdit(self.frame_viewport)
        self.nome_arquivo_entrada.setGeometry(QtCore.QRect(500, 225, 150, 30))
        self.nome_arquivo_entrada.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.nome_arquivo_entrada.setObjectName("label_arquivo_entrada")
        self.nome_arquivo_entrada.setPlaceholderText("Nome para abrir arquivo")

        self.nome_arquivo_saida = QLineEdit(self.frame_viewport)
        self.nome_arquivo_saida.setGeometry(QtCore.QRect(745, 225, 150, 30))
        self.nome_arquivo_saida.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.nome_arquivo_saida.setObjectName("label_arquivo_saida")
        self.nome_arquivo_saida.setPlaceholderText("Nome do novo arquivo")

        self.verticalLayout.addWidget(self.frame_viewport)

        MainDisplay.setCentralWidget(self.centralwidget)

        # Configurando os botoes
        self.adicionar_button.clicked.connect(self.pop_up_digitar_pontos)
        self.ler_arquivo_button.clicked.connect(self.ler_arquivo)
        self.gerar_arquivo_button.clicked.connect(self.gerar_arquivo)
        self.operacoes_button.clicked.connect(self.pop_up_realizar_operacao)
        self.right_button.clicked.connect(self.move_direita)
        self.left_button.clicked.connect(self.move_esquerda)
        self.up_button.clicked.connect(self.move_cima)
        self.down_button.clicked.connect(self.move_baixo)
        self.zoom_in_button.clicked.connect(self.ZoomIn)
        self.zoom_out_button.clicked.connect(self.ZoomOut)
        self.anticlockwise_rotation_button.clicked.connect(self.rotaciona_antihorario)
        self.clockwise_rotation_button.clicked.connect(self.rotaciona_horario)

        self.retranslateUi(MainDisplay)
        QtCore.QMetaObject.connectSlotsByName(MainDisplay)

    def retranslateUi(self, MainDisplay):
        _translate = QtCore.QCoreApplication.translate
        MainDisplay.setWindowTitle(_translate("MainDisplay", "Sistema Gráfico 2D"))
        self.up_button.setText(_translate("MainDisplay", "▲"))
        self.down_button.setText(_translate("MainDisplay", "▼"))
        self.right_button.setText(_translate("MainDisplay", "►"))
        self.left_button.setText(_translate("MainDisplay", "◄"))
        self.zoom_in_button.setStyleSheet("font-size: 20px;")
        self.zoom_in_button.setText(_translate("MainDisplay", "\u2315+"))
        self.zoom_out_button.setStyleSheet("font-size: 20px;")
        self.zoom_out_button.setText(_translate("MainDisplay", "\u2315-"))
        self.anticlockwise_rotation_button.setStyleSheet("font-size: 20px;")
        self.anticlockwise_rotation_button.setText(_translate("MainDisplay", "⭯"))
        self.clockwise_rotation_button.setStyleSheet("font-size: 20px;")
        self.clockwise_rotation_button.setText(_translate("MainDisplay", "⭮"))
        self.texto_controle_window.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Controle da Window</span></p></body></html>',
            )
        )
        self.texto_gerenciar_arquivos.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Gerenciar Arquivos</span></p></body></html>',
            )
        )
        self.texto_gerenciar_objetos.setHtml(
            _translate(
                "MainDisplay",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Gerenciar Objetos</span></p></body></html>',
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
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Viewport</span></p></body></html>',
            )
        )
        self.adicionar_button.setText(_translate("MainDisplay", "Adicionar"))
        self.ler_arquivo_button.setText(_translate("MainDisplay", "Abrir"))
        self.gerar_arquivo_button.setText(_translate("MainDisplay", "Salvar"))
        self.operacoes_button.setText(_translate("MainDisplay", "Operações"))

    def quantidade_de_pontos(self):
        qtdPontos = numero_pontosDialog()
        x = qtdPontos.exec_()
        if qtdPontos.submitted:
            return qtdPontos.numero_pontos()
        return -1

    def pedir_cores(self):
        cores = recolorirDialog()
        x = cores.exec_()
        if cores.submitted:
            return cores.cores()
        return (-1, -1, -1)

    def pop_up_digitar_pontos(self):
        error = False

        if self.AdicionarObjetos.currentText() == "Wireframe":
            # Abre uma janela secundaria perguntando quantos pontos tem o poligono
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
            # Aqui roda apos "fechar a janela, mas ainda eh possivel acessar seus atributos"
            if getCoordenadas.submitted:
                if self.AdicionarObjetos.currentText() == "Ponto":
                    elemento_grafico = Ponto(
                        getCoordenadas.dict_info["nome"],
                        getCoordenadas.dict_info["cor"],
                        getCoordenadas.dict_info["coordenadas"],
                    )

                elif self.AdicionarObjetos.currentText() == "Reta":
                    elemento_grafico = Reta(
                        getCoordenadas.dict_info["nome"],
                        getCoordenadas.dict_info["cor"],
                        getCoordenadas.dict_info["coordenadas"],
                    )

                else:
                    elemento_grafico = Wireframe(
                        getCoordenadas.dict_info["nome"],
                        getCoordenadas.dict_info["cor"],
                        getCoordenadas.dict_info["coordenadas"],
                    )


                self.display_file.adicionar(elemento_grafico)
                self.resetar_desenhos()
                # Adicionando objeto criado na lista de objetos
                self.ListaDeObjetos.addItem(getCoordenadas.dict_info["nome"])

    def pop_up_realizar_operacao(self):
        fazOperacao = QMessageBox()
        fazOperacao.setWindowTitle("Operações")
        fazOperacao.setText("Escolha a operação a ser realizada")
        fazOperacao.setStyleSheet("background-color: rgb(165,165,165);")

        # Criando os botoes
        fazOperacao.setStandardButtons(
            QMessageBox.Ok | QMessageBox.Save | QMessageBox.Open | QMessageBox.Cancel
        )

        # Renomeando o botao de troca de cor
        botao_cor = fazOperacao.button(QMessageBox.Ok)
        botao_cor.setText("Recolorir Objeto")
        botao_cor.setFixedSize(150, 30)
        botao_cor.setStyleSheet("background-color: rgb(212,208,200);")

        # Renomeando o botao de realizar transformacao 2D
        botao_transformacao = fazOperacao.button(QMessageBox.Save)
        botao_transformacao.setText("Transformações 2D")
        botao_transformacao.setFixedSize(150, 30)
        botao_transformacao.setStyleSheet("background-color: rgb(212,208,200);")

        # Renomeando o botao de deletar objeto
        botao_deletar = fazOperacao.button(QMessageBox.Open)
        botao_deletar.setText("Deletar Objeto")
        botao_deletar.setFixedSize(150, 30)
        botao_deletar.setStyleSheet("background-color: rgb(212,208,200);")

        # Renomeando o botao de cancelar
        botao_cancelar = fazOperacao.button(QMessageBox.Cancel)
        botao_cancelar.setText("Cancelar")
        botao_cancelar.setFixedSize(150, 30)
        botao_cancelar.setStyleSheet("background-color: rgb(212,208,200);")

        fazOperacao.setDefaultButton(QMessageBox.Cancel)

        i = fazOperacao.exec_()

        if i == QMessageBox.Ok:
            self.recolorir_objeto()
        elif i == QMessageBox.Save:
            self.escolher_transformacao_2D()
        elif i == QMessageBox.Open:
            self.deletar_objeto()
        else:
            pass

        """
        QMessageBox.Ok
        QMessageBox.Save
        QMessageBox.Open
        QMessageBox.Cancel
        QMessageBox.Close
        QMessageBox.Apply
        QMessageBox.Reset
        QMessageBox.RestoreDefaults
        QMessageBox.Help
        QMessageBox.SaveAll
        QMessageBox.Yes
        QMessageBox.No
        QMessageBox.YesToAll
        QMessageBox.NoToAll
        QMessageBox.Abort
        QMessageBox.Retry
        QMessageBox.Ignore
        """

    def escolher_transformacao_2D(self):
        if self.ListaDeObjetos.count() > 0:
            transf = transformacaoDialog()
            x = transf.exec_()
            if transf.submitted:
                coordenadas_atualizadas = []

                # Obtendo o objeto desejado
                i = self.ListaDeObjetos.currentIndex()
                elemento_grafico = self.display_file.getElementoGrafico(i)

                if transf.transformacao["transformacao"] == "translacao":
                    (desvio_x, desvio_y) = transf.transformacao["argumento"][0]

                    matriz_translacao = np.array(
                        [[1, 0, 0], [0, 1, 0], [desvio_x, desvio_y, 1]]
                    )

                    for i, j in elemento_grafico.get_coordenadas():
                        pontos = np.array([[i, j, 1]])
                        pontos_atualizados = np.dot(pontos, matriz_translacao)

                        coordenadas_atualizadas.append(
                            (pontos_atualizados[0][0], pontos_atualizados[0][1])
                        )

                    # Atualiza as coordenadas
                    elemento_grafico.set_coordenadas(coordenadas_atualizadas)

                elif transf.transformacao["transformacao"] == "rotacao":
                    angulo = radians(
                        -transf.transformacao["argumento"][0]
                    )  # Angulo em radianos
                    (x_rot, y_rot) = transf.transformacao["argumento"][1]
                    dx, dy = (None, None)  # desvios.

                    if y_rot == "origem":
                        dx, dy = 0, 0
                    elif y_rot == "centro_objeto":
                        (cx, cy) = elemento_grafico.get_centro()
                        dx, dy = cx, cy
                    else:
                        # Funciona
                        dx = x_rot
                        dy = y_rot

                    matriz_translacao1 = np.array([[1, 0, 0], [0, 1, 0], [-dx, -dy, 1]])

                    matriz_rotacao = np.array(
                        [
                            [cos(angulo), -sin(angulo), 0],
                            [sin(angulo), cos(angulo), 0],
                            [0, 0, 1],
                        ]
                    )

                    matriz_translacao2 = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])

                    matriz_resultante = FormulasMatematicas.junta_matrizes(
                        matriz_translacao1, matriz_rotacao, matriz_translacao2
                    )

                    for i, j in elemento_grafico.get_coordenadas():
                        pontos = np.array([[i, j, 1]])
                        pontos_atualizados = np.dot(pontos, matriz_resultante)

                        coordenadas_atualizadas.append(
                            (pontos_atualizados[0][0], pontos_atualizados[0][1])
                        )

                    # Atualiza as coordenadas
                    elemento_grafico.set_coordenadas(coordenadas_atualizadas)

                else:  # eh escalonamento
                    (cx, cy) = elemento_grafico.get_centro()
                    coef_escalonamento = transf.transformacao["argumento"][0]

                    if coef_escalonamento == 0:
                        transf.aviso_escalonamento_zero()
                    else:
                        matriz_traz_ao_centro = np.array(
                            [[1, 0, 0], [0, 1, 0], [-cx, -cy, 1]]
                        )
                        matriz_escalona = np.array(
                            [
                                [coef_escalonamento, 0, 0],
                                [0, coef_escalonamento, 0],
                                [0, 0, 1],
                            ]
                        )
                        matriz_devolve_ao_local_original = np.array(
                            [[1, 0, 0], [0, 1, 0], [cx, cy, 1]]
                        )

                        matriz_resultante = FormulasMatematicas.junta_matrizes(
                            matriz_traz_ao_centro,
                            matriz_escalona,
                            matriz_devolve_ao_local_original,
                        )

                        for i, j in elemento_grafico.get_coordenadas():
                            pontos = np.array([[i, j, 1]])
                            pontos_atualizados = np.dot(pontos, matriz_resultante)

                            coordenadas_atualizadas.append(
                                (pontos_atualizados[0][0], pontos_atualizados[0][1])
                            )

                        # Atualiza as coordenadas
                        elemento_grafico.set_coordenadas(coordenadas_atualizadas)

                # atualizando desenhos
                self.resetar_desenhos()

    def recolorir_objeto(self):
        if self.ListaDeObjetos.count() > 0:
            cores = self.pedir_cores()
            if cores != (-1, -1, -1):
                # Obtendo o objeto desejado
                i = self.ListaDeObjetos.currentIndex()
                elemento_grafico = self.display_file.getElementoGrafico(i)

                # Modificando a cor em RGB
                elemento_grafico.set_cor(cores)

                # Redesenhando
                self.resetar_desenhos()

    def deletar_objeto(self):
        # Deleta o objeto selecionado
        if self.ListaDeObjetos.count() > 0:
            # Obtendo o objeto desejado
            i = self.ListaDeObjetos.currentIndex()

            # Removendo objeto da lista da interface
            self.ListaDeObjetos.removeItem(i)

            # Removendo objeto do display file
            self.display_file.remover(i)

            # Redesenhando
            self.resetar_desenhos()

    def desenhar_objeto(self, elemento_grafico):
        if elemento_grafico.get_tipo() == "Ponto":
            self.desenhar_ponto(elemento_grafico)
        elif elemento_grafico.get_tipo() == "Reta":
            self.desenhar_reta(elemento_grafico)
        elif elemento_grafico.get_tipo() == "Wireframe":
            self.desenhar_wireframe(elemento_grafico)

    def resetar_desenhos(self):
        # Preenchendo tela de branco
        canvas = QtGui.QPixmap(451, 461)
        canvas.fill(Qt.white)
        self.area_desenho.setPixmap(canvas)

        self.display_file.calculaNormalizadas(self.window)


        # Redesenhando todos os objetos
        for objeto in self.display_file.getListaElementosGraficos():
            self.desenhar_objeto(objeto)

    def desenhar_ponto(self, ponto: Ponto):
        painter = QtGui.QPainter(self.area_desenho.pixmap())

        # Definindo cor e tamanho do ponto
        cor = QtGui.QColor(int(ponto.cor[0]), int(ponto.cor[1]), int(ponto.cor[2]))
        pen = QtGui.QPen(cor, 5)
        painter.setPen(pen)

        # Recalculando o X
        coordenadaX = int(
            FormulasMatematicas.calcular_x_viewport(
                ponto.get_coordenadas_normalizadas()[0][0], self.window
            )
        )

        # Recalculando o Y
        coordenadaY = int(
            FormulasMatematicas.calcular_y_viewport(
                ponto.get_coordenadas_normalizadas()[0][1], self.window
            )
        )

        # Desenhando o ponto
        painter.drawPoint(coordenadaX, coordenadaY)
        painter.end()

    def desenhar_reta(self, reta: Reta):
        pontos = reta.get_coordenadas_normalizadas()
        painter = QtGui.QPainter(self.area_desenho.pixmap())

        # Definindo a cor e tamanho da reta
        cor = QtGui.QColor(int(reta.cor[0]), int(reta.cor[1]), int(reta.cor[2]))
        pen = QtGui.QPen(cor, 5)
        painter.setPen(pen)

        # Desenhando a reta
        painter.drawLine(
            int(FormulasMatematicas.calcular_x_viewport(pontos[0][0], self.window)),
            int(FormulasMatematicas.calcular_y_viewport(pontos[0][1], self.window)),
            int(FormulasMatematicas.calcular_x_viewport(pontos[1][0], self.window)),
            int(FormulasMatematicas.calcular_y_viewport(pontos[1][1], self.window)),
        )
        painter.end()

    def desenhar_wireframe(self, wireframe: Wireframe):
        pontos = wireframe.get_coordenadas_normalizadas()
        painter = QtGui.QPainter(self.area_desenho.pixmap())

        # Definindo a cor e tamanho do wireframe
        cor = QtGui.QColor(
            int(wireframe.cor[0]), int(wireframe.cor[1]), int(wireframe.cor[2])
        )
        pen = QtGui.QPen(cor, 5)
        painter.setPen(pen)

        for i in range(len(pontos)):
            if i != (len(pontos) - 1):
                painter.drawLine(
                    int(
                        FormulasMatematicas.calcular_x_viewport(
                            pontos[i][0], self.window
                        )
                    ),
                    int(
                        FormulasMatematicas.calcular_y_viewport(
                            pontos[i][1], self.window
                        )
                    ),
                    int(
                        FormulasMatematicas.calcular_x_viewport(
                            pontos[i + 1][0], self.window
                        )
                    ),
                    int(
                        FormulasMatematicas.calcular_y_viewport(
                            pontos[i + 1][1], self.window
                        )
                    ),
                )
            else:
                painter.drawLine(
                    int(
                        FormulasMatematicas.calcular_x_viewport(
                            pontos[i][0], self.window
                        )
                    ),
                    int(
                        FormulasMatematicas.calcular_y_viewport(
                            pontos[i][1], self.window
                        )
                    ),
                    int(
                        FormulasMatematicas.calcular_x_viewport(
                            pontos[0][0], self.window
                        )
                    ),
                    int(
                        FormulasMatematicas.calcular_y_viewport(
                            pontos[0][1], self.window
                        )
                    ),
                )

        painter.end()

    def move_direita(self):
        self.window.moveuDireita()
        self.resetar_desenhos()  # Redesenha o viewport

    def move_esquerda(self):
        self.window.moveuEsquerda()
        self.resetar_desenhos()  # Redesenha o viewport

    def move_cima(self):
        self.window.moveuCima()
        self.resetar_desenhos()  # Redesenha o viewport

    def move_baixo(self):
        self.window.moveuBaixo()
        self.resetar_desenhos()  # Redesenha o viewport

    def ZoomIn(self):
        self.window.ZoomIn()
        self.resetar_desenhos()  # Redesenha o viewport

    def ZoomOut(self):
        self.window.ZoomOut()
        self.resetar_desenhos()  # Redesenha o viewport

    def rotaciona_antihorario(self):
        print("Rotaciona Anti-horário")
        self.resetar_desenhos()  # Redesenha o viewport

    def rotaciona_horario(self):
        print("Rotaciona Horário")
        self.resetar_desenhos()  # Redesenha o viewport

    def ler_arquivo(self):
        nome_arquivo = self.nome_arquivo_entrada.text()

        if nome_arquivo.replace(" ", "") == "":
            return

        if not exists(nome_arquivo):
            self.arquivo_nao_encontrado()
            return

        nome_base, extensao = splitext(nome_arquivo)
        if extensao != ".obj":
            self.extensao_invalida()
            return

        with open(nome_arquivo, "r") as arquivo:
            linha = arquivo.readline()
            while linha:
                palavras = linha.split(" ")
                if palavras[0] == "mtllib":
                    nome_mtl = palavras[1].strip()
                linha = arquivo.readline()

        if not exists(nome_mtl):
            self.arquivo_nao_encontrado()
            return

        nome_base, extensao = splitext(nome_mtl)
        if extensao != ".mtl":
            self.extensao_invalida()
            return

        leitor = LeitorOBJ(nome_arquivo)

        for key, val in leitor.elementos_graficos.items():
            i = 2
            nome = key.strip()
            while nome in self.display_file.getNomesElementosGraficos():
                if i > 2:
                    novo_nome = list(nome)
                    novo_nome[-1] = str(i)
                    nome = "".join(novo_nome)
                else:
                    nome = nome + "_" + str(i)
                i += 1
            if val[0] == "Ponto":
                elemento_grafico = Ponto(
                    nome,
                    val[1],
                    self.obter_vertices(val[2], leitor.vertices),
                )

            elif val[0] == "Reta":
                elemento_grafico = Reta(
                    nome,
                    val[1],
                    self.obter_vertices(val[2], leitor.vertices),
                )

            else:
                elemento_grafico = Wireframe(
                    nome,
                    val[1],
                    self.obter_vertices(val[2], leitor.vertices),
                )


            self.display_file.adicionar(elemento_grafico)
            self.ListaDeObjetos.addItem(nome)
        self.resetar_desenhos()

    def obter_vertices(self, indices, vertices):
        v = []
        for indice in indices:
            # Alterar quando for usar uma coordenada a mais
            v.append((vertices[indice - 1][0], vertices[indice - 1][1]))
        return v

    def arquivo_nao_encontrado(self):
        nao_encontrado = QMessageBox()
        nao_encontrado.setWindowTitle("Aviso!")
        nao_encontrado.setText("O arquivo requisitado não foi encontrado")
        nao_encontrado.setStyleSheet("background-color: rgb(212,208,200);")
        nao_encontrado.setStandardButtons(QMessageBox.Ok)
        botao_ok = nao_encontrado.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")
        nao_encontrado.setIcon(QMessageBox.Warning)

        i = nao_encontrado.exec_()

    def extensao_invalida(self):
        invalida = QMessageBox()
        invalida.setWindowTitle("Aviso!")
        invalida.setText("O arquivo não possui extensão .obj ou .mtl")
        invalida.setStyleSheet("background-color: rgb(212,208,200);")
        invalida.setStandardButtons(QMessageBox.Ok)
        botao_ok = invalida.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")
        invalida.setIcon(QMessageBox.Warning)

        i = invalida.exec_()

    def gerar_arquivo(self):
        nome_arquivo = self.nome_arquivo_saida.text()

        if nome_arquivo.replace(" ", "") == "":
            return

        if nome_arquivo[-4:] != ".obj":
            self.extensao_invalida()
            return

        if exists(nome_arquivo):
            if not self.arquivo_encontrado():
                return

        if exists("cores.mtl"):
            nome_base, extensao = splitext("cores.mtl")
            if extensao == ".mtl":
                if not self.arquivo_encontrado():
                    return

        objetos, vertices = self.gerar_lista_vertices()

        gerador = GeradorOBJ(nome_arquivo, objetos, vertices)
        gerador.gerarArquivoOBJ()

    def gerar_lista_vertices(self):
        objetos = {}
        vertices = []
        for objeto in self.display_file.lista_elementos_graficos:
            objetos[objeto.get_nome()] = ["", (), []]
            for ponto in objeto.get_coordenadas():
                if ponto not in vertices:
                    vertices.append(ponto)
                if objeto.get_tipo() == "Ponto":
                    objetos[objeto.get_nome()][0] = "p"
                else:
                    objetos[objeto.get_nome()][0] = "l"
                objetos[objeto.get_nome()][1] = objeto.get_cor()
                objetos[objeto.get_nome()][2].append(vertices.index(ponto) + 1)
        return objetos, vertices

    def arquivo_encontrado(self) -> bool:
        encontrado = QMessageBox()
        encontrado.setWindowTitle("Atenção!")
        encontrado.setText("O arquivo requisitado será sobrescrito")
        encontrado.setStyleSheet("background-color: rgb(165,165,165);")
        encontrado.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        botao_ok = encontrado.button(QMessageBox.Ok)
        botao_ok.setStyleSheet("background-color: rgb(212,208,200);")
        botao_cancel = encontrado.button(QMessageBox.Cancel)
        botao_cancel.setStyleSheet("background-color: rgb(212,208,200);")
        encontrado.setIcon(QMessageBox.Information)

        x = encontrado.exec_()

        if x == QMessageBox.Ok:
            return True
        else:
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainDisplay = QtWidgets.QMainWindow()
    ui = Ui_MainDisplay()
    ui.setupUi(MainDisplay)
    MainDisplay.show()
    sys.exit(app.exec_())
