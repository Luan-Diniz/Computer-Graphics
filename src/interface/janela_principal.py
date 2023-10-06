from math import atan2

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QPen, QPixmap
from PyQt5.QtWidgets import QMessageBox

from src.dialogs.adicionar_objeto import AdicionarObjetoDialog
from src.dialogs.quantidade_de_pontos import QuantidadeDePontosDialog
from src.dialogs.recolorir_objeto import RecolorirObjetoDialog
from src.dialogs.transformacoes import TransformacoesDialog
from src.interface.ui_main_display import Ui_MainDisplay
from src.math.clipping import Clipping
from src.math.object_operations import ObjectOperations
from src.math.viewport_operations import ViewportOperations
from src.messages.operacoes import OperacoesMessage
from src.messages.troca_clipping import TrocaClippingMessage
from src.objects.figuras_geometricas import Curva, Ponto, Reta, Wireframe
from src.objects.gerador_obj import GeradorOBJ
from src.objects.leitor_obj import LeitorOBJ


class JanelaPrincipal(Ui_MainDisplay):
    def pedir_quantidade_de_pontos(self, tipo: int):
        pontos = QuantidadeDePontosDialog(tipo)
        x = pontos.exec_()
        if pontos.submitted:
            return (pontos.numero_pontos(), pontos.poligono_preenchido())
        return (-1, False)

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

        if object_type == "Ponto":
            getCoordenadas = AdicionarObjetoDialog(
                1, self.display_file.getNomesElementosGraficos()
            )
        elif object_type == "Reta":
            getCoordenadas = AdicionarObjetoDialog(
                2, self.display_file.getNomesElementosGraficos()
            )
        elif object_type == "Wireframe":
            # Abre uma janela secundaria perguntando quantos pontos tem o poligono
            qtd_pontos, preenchido = self.pedir_quantidade_de_pontos(0)
            if qtd_pontos != -1:
                getCoordenadas = AdicionarObjetoDialog(
                    qtd_pontos, self.display_file.getNomesElementosGraficos()
                )
            else:
                error = True
        elif object_type == "Curva":
            # Abre uma janela secundaria perguntando quantos pontos tem o poligono
            qtd_pontos, preenchido = self.pedir_quantidade_de_pontos(1)
            if qtd_pontos != -1:
                getCoordenadas = AdicionarObjetoDialog(
                    qtd_pontos, self.display_file.getNomesElementosGraficos()
                )
            else:
                error = True

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
        elif i == QMessageBox.Abort:
            # trocar clipping utilizado
            if self.clipping_algorithm == "Cohen-Sutherland":
                self.clipping_algorithm = "Liang-Barsky"
            else:
                self.clipping_algorithm = "Cohen-Sutherland"

            aviso_troca_clipping = TrocaClippingMessage(self.clipping_algorithm)
            aviso_troca_clipping.exec_()

        elif i == QMessageBox.Open:
            self.deletar_objeto()
        else:
            pass

    def adicionar_objeto(self, tipo, nome, cor, coordenadas, preenchido):
        if tipo == "Ponto":
            elemento_grafico = Ponto(nome, cor, coordenadas)

        elif tipo == "Reta":
            elemento_grafico = Reta(nome, cor, coordenadas)

        elif tipo == "Wireframe":
            elemento_grafico = Wireframe(nome, cor, coordenadas, preenchido)

        elif tipo == "Curva":
            elemento_grafico = Curva(nome, cor, coordenadas)

        self.display_file.adicionar(elemento_grafico)
        self.ListaDeObjetos.addItem(nome)
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
        elif elemento_grafico.get_tipo() == "Curva":
            self.desenhar_curva(elemento_grafico)

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
        (Xwmin, Ywmin) = (self.window.Xwminnormalizado, self.window.Ywminnormalizado)
        (Xwmax, Ywmax) = (self.window.Xwmaxnormalizado, self.window.Ywmaxnormalizado)
        (Xnponto, Ynponto) = ponto.get_coordenadas_normalizadas()[0]

        if not Clipping.point_clippig(Xnponto, Ynponto, Xwmin, Xwmax, Ywmin, Ywmax):
            return

        # Recalculando o X
        coordenadaX = int(ViewportOperations.calcular_x_viewport(Xnponto, self.window))

        # Recalculando o Y
        coordenadaY = int(ViewportOperations.calcular_y_viewport(Ynponto, self.window))

        painter = QPainter(self.area_desenho.pixmap())
        painter.setRenderHints(painter.Antialiasing)

        # Definindo cor e tamanho do ponto
        cor = QColor(int(ponto.cor[0]), int(ponto.cor[1]), int(ponto.cor[2]))
        pen = QPen(cor, 3)
        painter.setPen(pen)

        # Desenhando o ponto
        painter.drawPoint(coordenadaX, coordenadaY)

    def desenhar_reta(self, reta: Reta):
        (Xwmin, Ywmin) = (self.window.Xwminnormalizado, self.window.Ywminnormalizado)
        (Xwmax, Ywmax) = (self.window.Xwmaxnormalizado, self.window.Ywmaxnormalizado)
        (Xnini, Ynini) = reta.get_coordenadas_normalizadas()[0]
        (Xnfin, Ynfin) = reta.get_coordenadas_normalizadas()[1]

        pontos = []
        if self.clipping_algorithm == "Cohen-Sutherland":  # Change to user options
            pontos = Clipping.cohen_sutherland(
                Xnini, Ynini, Xnfin, Ynfin, Xwmin, Xwmax, Ywmin, Ywmax
            )
        else:
            pontos = Clipping.liang_barsky(
                Xnini, Ynini, Xnfin, Ynfin, Xwmin, Xwmax, Ywmin, Ywmax
            )

        if pontos == []:
            return

        painter = QPainter(self.area_desenho.pixmap())
        painter.setRenderHints(painter.Antialiasing)

        # Definindo a cor e tamanho da reta
        cor = QColor(int(reta.cor[0]), int(reta.cor[1]), int(reta.cor[2]))
        pen = QPen(cor, 3)
        painter.setPen(pen)

        # Desenhando a reta
        painter.drawLine(
            int(ViewportOperations.calcular_x_viewport(pontos[0][0], self.window)),
            int(ViewportOperations.calcular_y_viewport(pontos[0][1], self.window)),
            int(ViewportOperations.calcular_x_viewport(pontos[1][0], self.window)),
            int(ViewportOperations.calcular_y_viewport(pontos[1][1], self.window)),
        )

    def desenhar_wireframe(self, wireframe: Wireframe):
        (Xwmin, Ywmin) = (self.window.Xwminnormalizado, self.window.Ywminnormalizado)
        (Xwmax, Ywmax) = (self.window.Xwmaxnormalizado, self.window.Ywmaxnormalizado)
        pontos_poligono = wireframe.get_coordenadas_normalizadas()

        pontos = Clipping.sutherland_hodgeman(
            pontos_poligono,
            [(Xwmin, Ywmin), (Xwmin, Ywmax), (Xwmax, Ywmax), (Xwmax, Ywmin)],
        )

        if pontos == []:
            return

        painter = QPainter(self.area_desenho.pixmap())
        painter.setRenderHints(painter.Antialiasing)
        path = QPainterPath()

        # Definindo a cor e tamanho do wireframe
        cor = QColor(
            int(wireframe.cor[0]), int(wireframe.cor[1]), int(wireframe.cor[2])
        )
        pen = QPen(cor, 3)
        painter.setPen(pen)

        if wireframe.preenchido:
            painter.setBrush(cor)

        for i in range(len(pontos)):
            if i == 0:
                path.moveTo(
                    int(
                        ViewportOperations.calcular_x_viewport(
                            pontos[0][0], self.window
                        )
                    ),
                    int(
                        ViewportOperations.calcular_y_viewport(
                            pontos[0][1], self.window
                        )
                    ),
                )
            else:
                path.lineTo(
                    int(
                        ViewportOperations.calcular_x_viewport(
                            pontos[i][0], self.window
                        )
                    ),
                    int(
                        ViewportOperations.calcular_y_viewport(
                            pontos[i][1], self.window
                        )
                    ),
                )
            if i == (len(pontos) - 1):
                path.lineTo(
                    int(
                        ViewportOperations.calcular_x_viewport(
                            pontos[0][0], self.window
                        )
                    ),
                    int(
                        ViewportOperations.calcular_y_viewport(
                            pontos[0][1], self.window
                        )
                    ),
                )
        path.closeSubpath()
        painter.drawPath(path)

    def desenhar_curva(self, curva: Curva):
        (Xwmin, Ywmin) = (self.window.Xwminnormalizado, self.window.Ywminnormalizado)
        (Xwmax, Ywmax) = (self.window.Xwmaxnormalizado, self.window.Ywmaxnormalizado)
        pontos_curva = curva.get_coordenadas_normalizadas()

        # Realizando o clipping da curva
        pontos = []

        if pontos == []:
            return

        painter = QPainter(self.area_desenho.pixmap())
        painter.setRenderHints(painter.Antialiasing)
        path = QPainterPath()

        # Definindo a cor e tamanho da curva
        cor = QColor(int(curva.cor[0]), int(curva.cor[1]), int(curva.cor[2]))
        pen = QPen(cor, 3)
        painter.setPen(pen)

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
