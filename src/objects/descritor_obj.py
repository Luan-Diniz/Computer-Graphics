from os.path import exists, splitext

from PyQt5.QtWidgets import QMessageBox
from src.messages.arquivo_encontrado import ArquivoEncontradoMessage
from src.messages.arquivo_nao_encontrado import ArquivoNaoEncontradoMessage
from src.messages.extensao_invalida import ExtensaoInvalidaMessage


class DescritorOBJ:
    def __init__(self):
        pass

    def verificar_nome_leitura(self, nome_arquivo):
        nome_arquivo = "data/wavefront/" + nome_arquivo

        if nome_arquivo.replace(" ", "") == "":
            return True

        if not exists(nome_arquivo):
            self.arquivo_nao_encontrado(nome_arquivo)
            return True

        nome_base, extensao = splitext(nome_arquivo)
        if extensao != ".obj":
            self.extensao_invalida(nome_arquivo, ".obj")
            return True

        with open(nome_arquivo, "r") as arquivo:
            linha = arquivo.readline()
            while linha:
                palavras = linha.split(" ")
                if palavras[0] == "mtllib":
                    nome_mtl = palavras[1].strip()
                linha = arquivo.readline()

        nome_mtl = "data/wavefront/" + nome_mtl

        if not exists(nome_mtl):
            self.arquivo_nao_encontrado(nome_mtl)
            return True

        nome_base, extensao = splitext(nome_mtl)
        if extensao != ".mtl":
            self.extensao_invalida(nome_mtl, ".mtl")
            return True

        return False

    def verificar_nome_escrita(self, nome_arquivo):
        if nome_arquivo.replace(" ", "") == "":
            return True

        if nome_arquivo[-4:] != ".obj":
            self.extensao_invalida(nome_arquivo, ".obj")
            return True

        if exists(nome_arquivo):
            if not self.arquivo_encontrado(nome_arquivo):
                return True

        if exists("data/wavefront/cores.mtl"):
            nome_base, extensao = splitext("data/wavefront/cores.mtl")
            if extensao == ".mtl":
                if not self.arquivo_encontrado(nome_arquivo):
                    return True

        return False

    def arquivo_encontrado(self, nome) -> bool:
        encontrado = ArquivoEncontradoMessage(nome)
        x = encontrado.exec_()
        if x == QMessageBox.Ok:
            return True
        else:
            return False

    def arquivo_nao_encontrado(self, nome):
        nao_encontrado = ArquivoNaoEncontradoMessage(nome)
        i = nao_encontrado.exec_()

    def extensao_invalida(self, nome, extensao):
        invalida = ExtensaoInvalidaMessage(nome, extensao)
        i = invalida.exec_()
