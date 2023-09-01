class DescritorOBJ:
    def __init__(self, nome_arquivo):
        vertices, elementos_graficos = self.lerArquivoOBJ(nome_arquivo)
        print("Vértices:", vertices)
        print("Elementos gráficos:", elementos_graficos)

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
                    cores[nome] = [rgb]
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
                elif palavras[0].isnumeric():
                    tipo, pontos = self.decidirTipo(palavras)
                    elementos_graficos[nome] = [tipo, cor, pontos]
                elif palavras[0] == "f":
                    tipo = "Face"
                    pontos = self.lerFace(palavras)
                    elementos_graficos[nome] = [tipo, cor, pontos]
                elif palavras[0] == "mtllib":
                    cores = self.lerArquivoMTL(palavras[1])
                elif palavras[0] == "usemtl":
                    cor = cores[palavras[1]]
            linha = arquivo.readline()

        return vertices, elementos_graficos

    def lerTupla(self, palavras: list) -> tuple:
        return (float(palavras[1]), float(palavras[2]), float(palavras[3]))

    def lerFace(self, palavras: list) -> list:
        pontos = []
        for ponto in palavras:
            pontos.append(int(pontos))
        return pontos

    def decidirTipo(self, palavras: str):
        tipo = ""
        pontos = []
        if len(palavras) == 2:
            tipo = "Reta"
        else:
            tipo = "Wireframe"
        for ponto in palavras:
            pontos.append(int(pontos))
        return tipo, pontos


d = DescritorOBJ("OBJ_teste.obj")
