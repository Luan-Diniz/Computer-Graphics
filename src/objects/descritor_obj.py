from os.path import exists, splitext

from src.messages.arquivo_encontrado import *
from src.messages.arquivo_nao_encontrado import *
from src.messages.extensao_invalida import *
from src.objects.figuras_geometricas import Ponto, Reta, Wireframe


class LeitorOBJ:
    def __init__(self, nome_arquivo):
        self.erro = self.verificar_nome(nome_arquivo)

        self.lista_objetos = self.abrir(nome_arquivo)

    def verificar_nome(self, nome_arquivo):
        if nome_arquivo.replace(" ", "") == "":
            return True

        if not exists(nome_arquivo):
            Avisos.arquivo_nao_encontrado()
            return True

        nome_base, extensao = splitext(nome_arquivo)
        if extensao != ".obj":
            Avisos.extensao_invalida()
            return True

        with open(nome_arquivo, "r") as arquivo:
            linha = arquivo.readline()
            while linha:
                palavras = linha.split(" ")
                if palavras[0] == "mtllib":
                    nome_mtl = palavras[1].strip()
                linha = arquivo.readline()

        if not exists(nome_mtl):
            Avisos.arquivo_nao_encontrado()
            return True

        nome_base, extensao = splitext(nome_mtl)
        if extensao != ".mtl":
            Avisos.extensao_invalida()
            return True

        return False

    def abrir(self, nome_arquivo, display_file):
        objetos = []
        vertices, elementos_graficos = self.lerArquivoOBJ(nome_arquivo)

        for key, val in elementos_graficos.items():
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
                    self.obter_vertices(val[2], vertices),
                )

            elif val[0] == "Reta":
                elemento_grafico = Reta(
                    nome,
                    val[1],
                    self.obter_vertices(val[2], vertices),
                )

            else:
                elemento_grafico = Wireframe(
                    nome,
                    val[1],
                    self.obter_vertices(val[2], vertices),
                )

            objetos.append(elemento_grafico)
        return objetos

    def obter_vertices(self, indices, vertices):
        v = []
        for indice in indices:
            # Alterar quando for usar uma coordenada a mais
            v.append((vertices[indice - 1][0], vertices[indice - 1][1]))
        return v

    def lerArquivoMTL(self, nome_arquivo: str) -> dict:
        cores = {}
        nome = ""
        rgb = ()

        with open(nome_arquivo, "r") as arquivo:
            linha = arquivo.readline()
            while linha:
                palavras = linha.split(" ")
                if palavras[0] == "Kd":
                    rgb = self.lerTupla(palavras)
                    cores[nome] = rgb
                elif palavras[0] == "newmtl":
                    nome = palavras[1]
                linha = arquivo.readline()

        return cores

    # O metodo a seguir le o arquivo .obj e insere os valores em suas respectivas listas
    def lerArquivoOBJ(self, nome_arquivo: str) -> dict:
        vertices = []

        elementos_graficos = {}
        nome = ""
        tipo = ""
        cor = ""
        pontos = []

        cores = {}

        with open(nome_arquivo, "r") as arquivo:
            linha = arquivo.readline()
            while linha:
                palavras = linha.split(" ")
                if palavras[0] == "v":
                    vertices.append(self.lerTupla(palavras))
                elif palavras[0] == "o":
                    nome = palavras[1]
                elif palavras[0] == "p":
                    tipo = "Ponto"
                    pontos.append(int(palavras[1]))
                    elementos_graficos[nome] = [tipo, cor, pontos]
                elif palavras[0] == "l":
                    tipo = self.decidirTipo(len(palavras))
                    pontos = self.lerLista(palavras[1:])
                    elementos_graficos[nome] = [tipo, cor, pontos]
                elif palavras[0] == "f":
                    tipo = "Face"
                    pontos = self.lerLista(palavras[1:])
                    elementos_graficos[nome] = [tipo, cor, pontos]
                elif palavras[0] == "mtllib":
                    cores = self.lerArquivoMTL(palavras[1].strip())
                elif palavras[0] == "usemtl":
                    cor = cores[palavras[1]]
                linha = arquivo.readline()

        return vertices, elementos_graficos

    def lerTupla(self, palavras: list) -> tuple:
        return (float(palavras[1]), float(palavras[2]), float(palavras[3]))

    def lerLista(self, palavras: list) -> list:
        pontos = []
        for ponto in palavras:
            pontos.append(int(ponto))
        return pontos

    def decidirTipo(self, tamanho: int) -> str:
        if tamanho == 2:
            return "Reta"
        return "Wireframe"


class GeradorOBJ:
    def __init__(self, nome_arquivo, elementos_graficos):
        if nome_arquivo.replace(" ", "") == "":
            return

        if nome_arquivo[-4:] != ".obj":
            Avisos.extensao_invalida()
            return

        if exists(nome_arquivo):
            if not Avisos.arquivo_encontrado():
                return

        if exists("cores.mtl"):
            nome_base, extensao = splitext("cores.mtl")
            if extensao == ".mtl":
                if not Avisos.arquivo_encontrado():
                    return

        objetos, vertices = self.gerar_lista_vertices(elementos_graficos)

        self.nome_arquivo = nome_arquivo
        self.objetos = objetos
        self.vertices = vertices
        self.cores = []

        self.gerarArquivoOBJ()

    def gerarArquivoOBJ(self):
        with open("cores.mtl", "w") as arquivo:
            arquivo.write("")
        with open(self.nome_arquivo, "w") as arquivo:
            for i in range(len(self.vertices)):
                saida = (
                    "v "
                    + str(self.vertices[i][0])
                    + " "
                    + str(self.vertices[i][1])
                    + " 0.0\n"
                )
                arquivo.write(saida)
            arquivo.write("mtllib cores.mtl\n\n")
            for key, val in self.objetos.items():
                nome = "o " + key + "\n"
                arquivo.write(nome)
                cor = self.gerarArquivoMTL(val[1])
                arquivo.write(cor)
                pontos = (
                    val[0]
                    + " "
                    + str(val[2]).replace("[", "").replace("]", "").replace(",", "")
                    + "\n"
                )
                arquivo.write(pontos)

    def gerarArquivoMTL(self, rgb):
        nova_cor = False
        if rgb not in self.cores:
            nova_cor = True
            self.cores.append(rgb)
        nome = "Cor_" + str(self.cores.index(rgb) + 1) + "\n"
        if nova_cor:
            with open("cores.mtl", "a") as arquivo:
                arquivo.write("newmtl " + nome)
                cor = (
                    "Kd " + str(rgb[0]) + " " + str(rgb[1]) + " " + str(rgb[2]) + "\n\n"
                )
                arquivo.write(cor)
        return "usemtl " + nome

    def gerar_lista_vertices(self, elementos_graficos):
        objetos = {}
        vertices = []
        for objeto in elementos_graficos:
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


class Avisos:
    @staticmethod
    def arquivo_encontrado() -> bool:
        encontrado = ArquivoEncontradoMessage()
        x = encontrado.exec_()
        if x == QMessageBox.Ok:
            return True
        else:
            return False

    @staticmethod
    def arquivo_nao_encontrado():
        nao_encontrado = ArquivoNaoEncontradoMessage()
        i = nao_encontrado.exec_()

    @staticmethod
    def extensao_invalida():
        invalida = ExtensaoInvalidaMessage()
        i = invalida.exec_()
