from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QComboBox,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from src.interface.display_file import DisplayFile
from src.interface.window import Window


class Ui_MainDisplay:
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

        self.clipping_algorithm = "cohen-sutherland"

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

        # Criando uma Label para o desenho dos Objetos
        self.area_desenho = QLabel("", self.frame_viewport)
        canvas = QPixmap(451, 461)
        canvas.fill(Qt.white)
        self.area_desenho.setPixmap(canvas)
        self.area_desenho.setGeometry(QRect(10, 40, 451, 461))

        # O frame do viewport começa no ponto (30, 60) e tem dimensões 411x421
        # Já a área de desenho começa em (10, 40) e tem dimensões 451x461
        self.viewport = QFrame(self.frame_viewport)
        self.viewport.setGeometry(QRect(30, 60, 411, 421))
        self.viewport.setMaximumSize(QSize(500, 500))
        self.viewport.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "border-color: rgb(255, 0, 0);\n"
            "border-width: 1.5px;\n"
            "border-style: solid;\n"
        )
        self.viewport.setFrameShape(QFrame.NoFrame)
        self.viewport.setFrameShadow(QFrame.Raised)
        self.viewport.setObjectName("viewport")

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
