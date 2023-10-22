from src.objects.descritor_obj import DescritorOBJ
from src.objects.figuras_geometricas import Ponto, Reta, Wireframe


class LeitorOBJ(DescritorOBJ):
    def __init__(self, nome_arquivo, display_file):
        self.erro = self.verificar_nome_leitura(nome_arquivo)
        if self.erro:
            return
        nome_arquivo = "data/wavefront/" + nome_arquivo
        self.lista_objetos = self.abrir(nome_arquivo, display_file)

    def abrir(self, nome_arquivo, display_file):
        objetos = []
        vertices, elementos_graficos = self.lerArquivoOBJ(nome_arquivo)

        for key, val in elementos_graficos.items():
            i = 2
            nome = key.strip()
            while nome in display_file.getNomesElementosGraficos():
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
                    nome, val[1], self.obter_vertices(val[2], vertices), val[3]
                )

            objetos.append(elemento_grafico)
        return objetos

    def obter_vertices(self, indices, vertices):
        v = []
        for indice in indices:
            v.append(
                (
                    vertices[indice - 1][0],
                    vertices[indice - 1][1],
                    vertices[indice - 1][2],
                )
            )
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
                    if tipo == "Wireframe":
                        # False se refere ao preenchimento ou nao do polígono.
                        elementos_graficos[nome] = [tipo, cor, pontos, False]
                    else:
                        elementos_graficos[nome] = [tipo, cor, pontos]
                elif palavras[0] == "f":
                    tipo = "Wireframe"
                    pontos = self.lerLista(palavras[1:])
                    # Poligono preenchido (True)
                    elementos_graficos[nome] = [tipo, cor, pontos, True]
                elif palavras[0] == "mtllib":
                    nome_mtl = "data/wavefront/" + palavras[1].strip()
                    cores = self.lerArquivoMTL(nome_mtl)
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
        if tamanho == 3:
            return "Reta"
        return "Wireframe"
