from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QPen, QPixmap
from PyQt5.QtWidgets import (
    QComboBox,
    QFrame,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from src.dialogs.adicionar_objeto import AdicionarObjetoDialog
from src.dialogs.quantidade_de_pontos import QuantidadeDePontosDialog
from src.dialogs.recolorir_objeto import RecolorirObjetoDialog
from src.dialogs.transformacoes import TransformacoesDialog
from src.interface.display_file import DisplayFile
from src.interface.window import Window
from src.math.interface_operations import InterfaceOperations
from src.math.object_operations import ObjectOperations
from src.messages.operacoes import OperacoesMessage
from src.objects.figuras_geometricas import Ponto, Reta, Wireframe
from src.objects.gerador_obj import GeradorOBJ
from src.objects.leitor_obj import LeitorOBJ


class Ui_MainDisplay(object):
    def setupUi(self, MainDisplay):
        MainDisplay.setObjectName("MainDisplay")
        MainDisplay.resize(960, 540)
        MainDisplay.setMinimumSize(QSize(960, 540))
        MainDisplay.setMaximumSize(QSize(960, 540))
        MainDisplay.setStyleSheet("background-color: rgb(212,208,200);")

        # Instanciando as classes
        self.window = Window()
        self.display_file = (
            DisplayFile()
        )  # Os elementos graficos ficarao guardados no Display File

        self.centralwidget = QWidget(MainDisplay)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_viewport = QFrame(self.centralwidget)
        self.frame_viewport.setStyleSheet("background-color: rgb(212, 208, 200);\n" "")
        self.frame_viewport.setFrameShape(QFrame.Panel)
        self.frame_viewport.setFrameShadow(QFrame.Raised)
        self.frame_viewport.setObjectName("frame_viewport")

        self.frame_movimentacao_window = QFrame(self.frame_viewport)
        self.frame_movimentacao_window.setGeometry(QRect(480, 350, 435, 150))
        self.frame_movimentacao_window.setStyleSheet(
            "background-color: rgb(165,165,165);"
        )
        self.frame_movimentacao_window.setMaximumSize(QSize(500, 500))
        self.frame_movimentacao_window.setFrameShape(QFrame.Box)
        self.frame_movimentacao_window.setFrameShadow(QFrame.Raised)
        self.frame_movimentacao_window.setObjectName("frame_movimentacao_window")

        self.frame_gerenciar_arquivos = QFrame(self.frame_viewport)
        self.frame_gerenciar_arquivos.setGeometry(QRect(480, 205, 435, 110))
        self.frame_gerenciar_arquivos.setStyleSheet(
            "background-color: rgb(165,165,165);"
        )
        self.frame_gerenciar_arquivos.setMaximumSize(QSize(500, 500))
        self.frame_gerenciar_arquivos.setFrameShape(QFrame.Box)
        self.frame_gerenciar_arquivos.setFrameShadow(QFrame.Raised)
        self.frame_gerenciar_arquivos.setObjectName("frame_gerenciar_arquivos")

        self.frame_gerenciar_objetos = QFrame(self.frame_viewport)
        self.frame_gerenciar_objetos.setGeometry(QRect(480, 55, 435, 120))
        self.frame_gerenciar_objetos.setStyleSheet(
            "background-color: rgb(165,165,165);"
        )
        self.frame_gerenciar_objetos.setMaximumSize(QSize(500, 500))
        self.frame_gerenciar_objetos.setFrameShape(QFrame.Box)
        self.frame_gerenciar_objetos.setFrameShadow(QFrame.Raised)
        self.frame_gerenciar_objetos.setObjectName("frame_gerenciar_objetos")

        self.up_button = QPushButton(self.frame_movimentacao_window)
        self.up_button.setGeometry(QRect(80, 10, 60, 30))
        self.up_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.up_button.setAutoDefault(False)
        self.up_button.setDefault(False)
        self.up_button.setFlat(False)
        self.up_button.setObjectName("up_button")

        self.down_button = QPushButton(self.frame_movimentacao_window)
        self.down_button.setGeometry(QRect(80, 110, 60, 30))
        self.down_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.down_button.setObjectName("down_button")

        self.right_button = QPushButton(self.frame_movimentacao_window)
        self.right_button.setGeometry(QRect(140, 60, 60, 30))
        self.right_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.right_button.setObjectName("right_button")

        self.left_button = QPushButton(self.frame_movimentacao_window)
        self.left_button.setGeometry(QRect(20, 60, 60, 30))
        self.left_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.left_button.setFlat(False)
        self.left_button.setObjectName("left_button")

        self.zoom_in_button = QPushButton(self.frame_movimentacao_window)
        self.zoom_in_button.setGeometry(QRect(250, 30, 60, 30))
        self.zoom_in_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.zoom_in_button.setObjectName("zoom_in_button")

        self.zoom_out_button = QPushButton(self.frame_movimentacao_window)
        self.zoom_out_button.setGeometry(QRect(250, 90, 60, 30))
        self.zoom_out_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.zoom_out_button.setObjectName("zoom_out_button")

        self.anticlockwise_rotation_button = QPushButton(self.frame_movimentacao_window)
        self.anticlockwise_rotation_button.setGeometry(QRect(355, 30, 60, 30))
        self.anticlockwise_rotation_button.setStyleSheet(
            "background-color: rgb(212, 208, 200);"
        )
        self.anticlockwise_rotation_button.setObjectName(
            "anticlockwise_rotation_button"
        )

        self.clockwise_rotation_button = QPushButton(self.frame_movimentacao_window)
        self.clockwise_rotation_button.setGeometry(QRect(355, 90, 60, 30))
        self.clockwise_rotation_button.setStyleSheet(
            "background-color: rgb(212, 208, 200);"
        )
        self.clockwise_rotation_button.setObjectName("clockwise_rotation_button")

        self.viewport = QFrame(self.frame_viewport)
        self.viewport.setGeometry(QRect(10, 40, 451, 461))
        self.viewport.setMaximumSize(QSize(500, 16777215))
        self.viewport.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "\n"
            "border-color: rgb(0, 0, 0);\n"
            "border-width : 1.2px;\n"
            "border-style:inset;\n"
            ""
        )
        self.viewport.setFrameShape(QFrame.NoFrame)
        self.viewport.setFrameShadow(QFrame.Raised)
        self.viewport.setObjectName("viewport")

        # Criando uma Label para o desenho dos Objetos
        self.area_desenho = QLabel("", self.frame_viewport)
        canvas = QPixmap(451, 461)
        canvas.fill(Qt.white)
        self.area_desenho.setPixmap(canvas)
        self.area_desenho.setGeometry(QRect(10, 40, 451, 461))

        self.texto_controle_window = QTextBrowser(self.frame_viewport)
        self.texto_controle_window.setGeometry(QRect(620, 325, 151, 21))
        self.texto_controle_window.setFrameShape(QFrame.NoFrame)
        self.texto_controle_window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_controle_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_controle_window.setObjectName("texto_controle_window")

        self.texto_gerenciar_arquivos = QTextBrowser(self.frame_viewport)
        self.texto_gerenciar_arquivos.setGeometry(QRect(620, 180, 151, 21))
        self.texto_gerenciar_arquivos.setFrameShape(QFrame.NoFrame)
        self.texto_gerenciar_arquivos.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_gerenciar_arquivos.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )
        self.texto_gerenciar_arquivos.setObjectName("texto_gerenciar_arquivos")

        self.texto_gerenciar_objetos = QTextBrowser(self.frame_viewport)
        self.texto_gerenciar_objetos.setGeometry(QRect(620, 30, 151, 21))
        self.texto_gerenciar_objetos.setFrameShape(QFrame.NoFrame)
        self.texto_gerenciar_objetos.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_gerenciar_objetos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_gerenciar_objetos.setObjectName("texto_gerenciar_objetos")

        self.ListaDeObjetos = QComboBox(self.frame_viewport)
        self.ListaDeObjetos.setGeometry(QRect(750, 90, 150, 30))
        self.ListaDeObjetos.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.ListaDeObjetos.setObjectName("ListaDeObjetos")

        self.AdicionarObjetos = QComboBox(self.frame_viewport)
        self.AdicionarObjetos.setGeometry(QRect(500, 90, 150, 30))
        self.AdicionarObjetos.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.AdicionarObjetos.setObjectName("AdicionarObjetos")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")
        self.AdicionarObjetos.addItem("")

        self.texto_adicionar_objeto = QTextBrowser(self.frame_viewport)
        self.texto_adicionar_objeto.setGeometry(QRect(490, 60, 120, 21))
        self.texto_adicionar_objeto.setStyleSheet("background-color: rgb(165,165,165);")
        self.texto_adicionar_objeto.setFrameShape(QFrame.NoFrame)
        self.texto_adicionar_objeto.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_adicionar_objeto.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_adicionar_objeto.setObjectName("texto_adicionar_objeto")

        self.texto_lista_objetos = QTextBrowser(self.frame_viewport)
        self.texto_lista_objetos.setGeometry(QRect(740, 60, 120, 21))
        self.texto_lista_objetos.setStyleSheet("background-color: rgb(165,165,165);")
        self.texto_lista_objetos.setFrameShape(QFrame.NoFrame)
        self.texto_lista_objetos.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_lista_objetos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_lista_objetos.setObjectName("texto_lista_objetos")

        self.texto_viewport = QTextBrowser(self.frame_viewport)
        self.texto_viewport.setGeometry(QRect(10, 10, 81, 21))
        self.texto_viewport.setFrameShape(QFrame.NoFrame)
        self.texto_viewport.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_viewport.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.texto_viewport.setObjectName("texto_viewport")

        self.adicionar_button = QPushButton(self.frame_viewport)
        self.adicionar_button.setGeometry(QRect(530, 135, 75, 30))
        self.adicionar_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.adicionar_button.setObjectName("adicionar_button")

        self.operacoes_button = QPushButton(self.frame_viewport)
        self.operacoes_button.setGeometry(QRect(780, 135, 75, 30))
        self.operacoes_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.operacoes_button.setObjectName("operacoes_button")

        self.ler_arquivo_button = QPushButton(self.frame_viewport)
        self.ler_arquivo_button.setGeometry(QRect(535, 270, 75, 30))
        self.ler_arquivo_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.ler_arquivo_button.setObjectName("ler_arquivo_button")

        self.gerar_arquivo_button = QPushButton(self.frame_viewport)
        self.gerar_arquivo_button.setGeometry(QRect(780, 270, 75, 30))
        self.gerar_arquivo_button.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.gerar_arquivo_button.setObjectName("gerar_arquivo_button")

        self.nome_arquivo_entrada = QLineEdit(self.frame_viewport)
        self.nome_arquivo_entrada.setGeometry(QRect(500, 225, 150, 30))
        self.nome_arquivo_entrada.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.nome_arquivo_entrada.setObjectName("label_arquivo_entrada")
        self.nome_arquivo_entrada.setPlaceholderText("Nome para abrir arquivo")

        self.nome_arquivo_saida = QLineEdit(self.frame_viewport)
        self.nome_arquivo_saida.setGeometry(QRect(745, 225, 150, 30))
        self.nome_arquivo_saida.setStyleSheet("background-color: rgb(212, 208, 200);")
        self.nome_arquivo_saida.setObjectName("label_arquivo_saida")
        self.nome_arquivo_saida.setPlaceholderText("Nome do novo arquivo")

        self.verticalLayout.addWidget(self.frame_viewport)

        MainDisplay.setCentralWidget(self.centralwidget)

        # Configurando os botoes
        self.adicionar_button.clicked.connect(self.pedir_pontos)
        self.ler_arquivo_button.clicked.connect(self.ler_arquivo)
        self.gerar_arquivo_button.clicked.connect(self.gerar_arquivo)
        self.operacoes_button.clicked.connect(self.pedir_operacao)
        self.right_button.clicked.connect(self.move_esquerda)
        self.left_button.clicked.connect(self.move_direita)
        self.up_button.clicked.connect(self.move_baixo)
        self.down_button.clicked.connect(self.move_cima)
        self.zoom_in_button.clicked.connect(self.ZoomIn)
        self.zoom_out_button.clicked.connect(self.ZoomOut)
        self.anticlockwise_rotation_button.clicked.connect(self.rotaciona_antihorario)
        self.clockwise_rotation_button.clicked.connect(self.rotaciona_horario)

        self.retranslateUi(MainDisplay)
        QMetaObject.connectSlotsByName(MainDisplay)

    def retranslateUi(self, MainDisplay):
        _translate = QCoreApplication.translate
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

    def pedir_quantidade_de_pontos(self):
        pontos = QuantidadeDePontosDialog()
        x = pontos.exec_()
        if pontos.submitted:
            return (pontos.numero_pontos(), pontos.poligono_preenchido())
        return -1

    def pedir_cores(self):
        cores = RecolorirObjetoDialog()
        x = cores.exec_()
        if cores.submitted:
            return cores.cores()
        return (-1, -1, -1)

    def pedir_pontos(self):
        preenchido = False
        error = False
        object_type = self.AdicionarObjetos.currentText()

        if object_type == "Wireframe":
            # Abre uma janela secundaria perguntando quantos pontos tem o poligono
            qtd_pontos, preenchido = self.pedir_quantidade_de_pontos()

            if qtd_pontos != -1:
                getCoordenadas = AdicionarObjetoDialog(
                    qtd_pontos, self.display_file.getNomesElementosGraficos()
                )
            else:
                error = True

        elif object_type == "Ponto":
            getCoordenadas = AdicionarObjetoDialog(
                1, self.display_file.getNomesElementosGraficos()
            )
        elif object_type == "Reta":
            getCoordenadas = AdicionarObjetoDialog(
                2, self.display_file.getNomesElementosGraficos()
            )

        if not error:
            x = getCoordenadas.exec_()
            # Aqui roda apos "fechar a janela, mas ainda eh possivel acessar seus atributos"
            if getCoordenadas.submitted:
                self.adicionar_objeto(
                    object_type,
                    getCoordenadas.dict_info["nome"],
                    getCoordenadas.dict_info["cor"],
                    getCoordenadas.dict_info["coordenadas"],
                    preenchido,
                )

    def pedir_operacao(self):
        operacao = OperacoesMessage()
        i = operacao.exec_()
        if i == QMessageBox.Ok:
            self.recolorir_objeto()
        elif i == QMessageBox.Save:
            self.escolher_transformacao_2D()
        elif i == QMessageBox.Open:
            self.deletar_objeto()
        else:
            pass

    def adicionar_objeto(self, type, name, color, coordinates, preenchido):
        if type == "Ponto":
            elemento_grafico = Ponto(name, color, coordinates)

        elif type == "Reta":
            elemento_grafico = Reta(name, color, coordinates)

        elif type == "Wireframe":
            elemento_grafico = Wireframe(name, color, coordinates, preenchido)

        self.display_file.adicionar(elemento_grafico)
        self.ListaDeObjetos.addItem(name)
        self.resetar_desenhos()

    def escolher_transformacao_2D(self):
        if self.ListaDeObjetos.count() > 0:
            transf = TransformacoesDialog()
            x = transf.exec_()
            if transf.submitted:
                # Obtendo o objeto desejado
                i = self.ListaDeObjetos.currentIndex()
                elemento_grafico = self.display_file.getElementoGrafico(i)
                transf_name = transf.transformacao["transformacao"]

                if transf_name == "translacao":
                    coordinates = transf.transformacao["argumento"][0]
                    ObjectOperations.translacao(elemento_grafico, coordinates)

                elif transf_name == "rotacao":
                    ObjectOperations.rotacao(
                        elemento_grafico,
                        transf.transformacao["argumento"][0],
                        transf.transformacao["argumento"][1],
                    )

                else:  # eh escalonamento
                    result = ObjectOperations.escalonamento(
                        elemento_grafico, transf.transformacao["argumento"][0]
                    )
                    if result == -1:
                        transf.aviso_escalonamento_zero()

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
        canvas = QPixmap(451, 461)
        canvas.fill(Qt.white)
        self.area_desenho.setPixmap(canvas)

        self.display_file.calculaNormalizadas(self.window)

        # Redesenhando todos os objetos
        for objeto in self.display_file.getListaElementosGraficos():
            self.desenhar_objeto(objeto)

    def desenhar_ponto(self, ponto: Ponto):
        painter = QPainter(self.area_desenho.pixmap())

        # Definindo cor e tamanho do ponto
        cor = QColor(int(ponto.cor[0]), int(ponto.cor[1]), int(ponto.cor[2]))
        pen = QPen(cor, 5)
        painter.setPen(pen)

        # Recalculando o X
        coordenadaX = int(
            InterfaceOperations.calcular_x_viewport(
                ponto.get_coordenadas_normalizadas()[0][0], self.window
            )
        )

        # Recalculando o Y
        coordenadaY = int(
            InterfaceOperations.calcular_y_viewport(
                ponto.get_coordenadas_normalizadas()[0][1], self.window
            )
        )

        # Desenhando o ponto
        painter.drawPoint(coordenadaX, coordenadaY)
        painter.end()

    def desenhar_reta(self, reta: Reta):
        pontos = reta.get_coordenadas_normalizadas()
        painter = QPainter(self.area_desenho.pixmap())

        # Definindo a cor e tamanho da reta
        cor = QColor(int(reta.cor[0]), int(reta.cor[1]), int(reta.cor[2]))
        pen = QPen(cor, 5)
        painter.setPen(pen)

        # Desenhando a reta
        painter.drawLine(
            int(InterfaceOperations.calcular_x_viewport(pontos[0][0], self.window)),
            int(InterfaceOperations.calcular_y_viewport(pontos[0][1], self.window)),
            int(InterfaceOperations.calcular_x_viewport(pontos[1][0], self.window)),
            int(InterfaceOperations.calcular_y_viewport(pontos[1][1], self.window)),
        )
        painter.end()

    def desenhar_wireframe(self, wireframe: Wireframe):
        pontos = wireframe.get_coordenadas_normalizadas()
        painter = QPainter(self.area_desenho.pixmap())
        path = QPainterPath()

        # Definindo a cor e tamanho do wireframe
        cor = QColor(
            int(wireframe.cor[0]), int(wireframe.cor[1]), int(wireframe.cor[2])
        )
        pen = QPen(cor, 5)
        painter.setPen(pen)

        if wireframe.preenchido:
            painter.setBrush(cor)

        for i in range(len(pontos)):
            if i != (len(pontos) - 1):
                path.moveTo(
                    int(
                        InterfaceOperations.calcular_x_viewport(
                            pontos[i][0], self.window
                        )
                    ),
                    int(
                        InterfaceOperations.calcular_y_viewport(
                            pontos[i][1], self.window
                        )
                    ),
                )
                path.lineTo(
                    int(
                        InterfaceOperations.calcular_x_viewport(
                            pontos[i + 1][0], self.window
                        )
                    ),
                    int(
                        InterfaceOperations.calcular_y_viewport(
                            pontos[i + 1][1], self.window
                        )
                    ),
                )
            else:
                path.lineTo(
                    int(
                        InterfaceOperations.calcular_x_viewport(
                            pontos[i][0], self.window
                        )
                    ),
                    int(
                        InterfaceOperations.calcular_y_viewport(
                            pontos[i][1], self.window
                        )
                    ),
                )
                path.lineTo(
                    int(
                        InterfaceOperations.calcular_x_viewport(
                            pontos[0][0], self.window
                        )
                    ),
                    int(
                        InterfaceOperations.calcular_y_viewport(
                            pontos[0][1], self.window
                        )
                    ),
                )
        painter.drawPath(path)
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
        self.window.rotacionaAntiHorario()
        self.resetar_desenhos()  # Redesenha o viewport

    def rotaciona_horario(self):
        self.window.rotatacionaHorario()
        self.resetar_desenhos()  # Redesenha o viewport

    def ler_arquivo(self):
        nome_arquivo = self.nome_arquivo_entrada.text()
        leitor = LeitorOBJ(nome_arquivo, self.display_file)
        if not leitor.erro:
            for objeto in leitor.lista_objetos:
                self.display_file.adicionar(objeto)
                self.ListaDeObjetos.addItem(objeto.get_nome())
            self.resetar_desenhos()

    def gerar_arquivo(self):
        nome_arquivo = self.nome_arquivo_saida.text()
        gerador = GeradorOBJ(nome_arquivo, self.display_file)
        if not gerador.erro:
            gerador.gerarArquivoOBJ()
