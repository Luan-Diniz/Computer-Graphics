from src.objects.descritor_obj import DescritorOBJ


class GeradorOBJ(DescritorOBJ):
    def __init__(self, nome_arquivo, display_file):
        self.erro = self.verificar_nome_escrita(nome_arquivo)
        if self.erro:
            return

        objetos, vertices = self.gerar_lista_vertices(display_file)

        self.nome_arquivo = nome_arquivo
        self.objetos = objetos
        self.vertices = vertices
        self.cores = []

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

    def gerar_lista_vertices(self, display_file):
        objetos = {}
        vertices = []
        for objeto in display_file.getListaElementosGraficos():
            objetos[objeto.get_nome()] = ["", (), []]
            for ponto in objeto.get_coordenadas():
                if ponto not in vertices:
                    vertices.append(ponto)
                if objeto.get_tipo() == "Ponto":
                    objetos[objeto.get_nome()][0] = "p"
                elif objeto.get_tipo() == "Wireframe" and objeto.preenchido:
                    objetos[objeto.get_nome()][0] = "f"
                else:
                    objetos[objeto.get_nome()][0] = "l"
                objetos[objeto.get_nome()][1] = objeto.get_cor()
                objetos[objeto.get_nome()][2].append(vertices.index(ponto) + 1)
        return objetos, vertices
