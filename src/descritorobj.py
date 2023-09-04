class LeitorOBJ:
    def __init__(self, nome_arquivo):
        self.vertices, self.elementos_graficos = self.lerArquivoOBJ(nome_arquivo)

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
    def __init__(self, nome_arquivo, objetos, vertices):
        self.nome_arquivo = nome_arquivo
        self.objetos = objetos
        self.vertices = vertices
        self.cores = []

    def gerarArquivoOBJ(self):
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
