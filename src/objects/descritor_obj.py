from os.path import exists, splitext

from PyQt5.QtWidgets import QMessageBox

from src.messages.arquivo_encontrado import ArquivoEncontradoMessage
from src.messages.arquivo_nao_encontrado import ArquivoNaoEncontradoMessage
from src.messages.extensao_invalida import ExtensaoInvalidaMessage


class DescritorOBJ:
    def __init__(self):
        pass

    def verificar_nome_leitura(self, nome_arquivo):
        if nome_arquivo.replace(" ", "") == "":
            return True

        if not exists(nome_arquivo):
            self.arquivo_nao_encontrado()
            return True

        nome_base, extensao = splitext(nome_arquivo)
        if extensao != ".obj":
            self.extensao_invalida()
            return True

        with open(nome_arquivo, "r") as arquivo:
            linha = arquivo.readline()
            while linha:
                palavras = linha.split(" ")
                if palavras[0] == "mtllib":
                    nome_mtl = palavras[1].strip()
                linha = arquivo.readline()

        if not exists(nome_mtl):
            self.arquivo_nao_encontrado()
            return True

        nome_base, extensao = splitext(nome_mtl)
        if extensao != ".mtl":
            self.extensao_invalida()
            return True

        return False

    def verificar_nome_escrita(self, nome_arquivo):
        if nome_arquivo.replace(" ", "") == "":
            return True

        if nome_arquivo[-4:] != ".obj":
            self.extensao_invalida()
            return True

        if exists(nome_arquivo):
            if not self.arquivo_encontrado():
                return True

        if exists("data/wavefront/cores.mtl"):
            nome_base, extensao = splitext("data/wavefront/cores.mtl")
            if extensao == ".mtl":
                if not self.arquivo_encontrado():
                    return True

        return False

    def arquivo_encontrado(self) -> bool:
        encontrado = ArquivoEncontradoMessage()
        x = encontrado.exec_()
        if x == QMessageBox.Ok:
            return True
        else:
            return False

    def arquivo_nao_encontrado(self):
        nao_encontrado = ArquivoNaoEncontradoMessage()
        i = nao_encontrado.exec_()

    def extensao_invalida(self):
        invalida = ExtensaoInvalidaMessage()
        i = invalida.exec_()
