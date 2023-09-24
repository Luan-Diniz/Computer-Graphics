import numpy as np


class Clipping:
    @staticmethod
    def point_clippig(Xnponto, Ynponto, Xwmin, Xwmax, Ywmin, Ywmax) -> bool:
        if (Xwmin <= Xnponto <= Xwmax) and (Ywmin <= Ynponto <= Ywmax):
            return True
        return False

    # - Cohen Sutherland ------------------------------------------------------------------------------------#
    @staticmethod
    def cohen_sutherland_calcular_codigo(X, Y, Xwmin, Xwmax, Ywmin, Ywmax):
        # Definindo códigos de região
        DENTRO = 0  # 0000
        ESQUERDA = 1  # 0001
        DIREITA = 2  # 0010
        ABAIXO = 4  # 0100
        ACIMA = 8  # 1000

        codigo = DENTRO
        if X < Xwmin:  # à esquerda do retângulo
            codigo |= ESQUERDA
        elif X > Xwmax:  # à direita do retângulo
            codigo |= DIREITA
        if Y < Ywmin:  # abaixo do retângulo
            codigo |= ABAIXO
        elif Y > Ywmax:  # acima do retângulo
            codigo |= ACIMA
        return codigo

    @staticmethod
    def cohen_sutherland(Xnini, Ynini, Xnfin, Ynfin, Xwmin, Xwmax, Ywmin, Ywmax):
        # Definindo códigos de região
        DENTRO = 0  # 0000
        ESQUERDA = 1  # 0001
        DIREITA = 2  # 0010
        ABAIXO = 4  # 0100
        ACIMA = 8  # 1000

        codigo1 = Clipping.cohen_sutherland_calcular_codigo(
            Xnini, Ynini, Xwmin, Xwmax, Ywmin, Ywmax
        )
        codigo2 = Clipping.cohen_sutherland_calcular_codigo(
            Xnfin, Ynfin, Xwmin, Xwmax, Ywmin, Ywmax
        )
        aceitar = False

        while True:
            # Se ambos os pontos finais estão dentro do retângulo
            if codigo1 == DENTRO and codigo2 == DENTRO:
                aceitar = True
                break

            # Se ambos os pontos finais estão fora do retângulo
            elif (codigo1 & codigo2) != DENTRO:
                break

            # Algum segmento está dentro do retângulo
            else:
                # A linha precisa ser recortada, pelo menos um dos pontos está fora
                X = 1.0
                Y = 1.0
                if codigo1 != DENTRO:
                    codigo_fora = codigo1
                else:
                    codigo_fora = codigo2

                # Encontrando o ponto de interseção por meio das fórmulas
                if codigo_fora & ACIMA:
                    # O ponto está acima do retângulo de recorte
                    X = Xnini + (Xnfin - Xnini) * (Ywmax - Ynini) / (Ynfin - Ynini)
                    Y = Ywmax
                elif codigo_fora & ABAIXO:
                    # O ponto está abaixo do retângulo de recorte
                    X = Xnini + (Xnfin - Xnini) * (Ywmin - Ynini) / (Ynfin - Ynini)
                    Y = Ywmin
                elif codigo_fora & DIREITA:
                    # O ponto está à direita do retângulo de recorte
                    Y = Ynini + (Ynfin - Ynini) * (Xwmax - Xnini) / (Xnfin - Xnini)
                    X = Xwmax
                elif codigo_fora & ESQUERDA:
                    # O ponto está à esquerda do retângulo de recorte
                    Y = Ynini + (Ynfin - Ynini) * (Xwmin - Xnini) / (Xnfin - Xnini)
                    X = Xwmin

                # Agora o ponto de interseção (X, Y) foi encontrado
                # Substituímos o ponto fora do retângulo de recorte pelo ponto de interseção
                if codigo_fora == codigo1:
                    Xnini = X
                    Ynini = Y
                    codigo1 = Clipping.cohen_sutherland_calcular_codigo(
                        Xnini, Ynini, Xwmin, Xwmax, Ywmin, Ywmax
                    )
                else:
                    Xnfin = X
                    Ynfin = Y
                    codigo2 = Clipping.cohen_sutherland_calcular_codigo(
                        Xnfin, Ynfin, Xwmin, Xwmax, Ywmin, Ywmax
                    )

        pontos = []
        if aceitar:
            pontos = [(Xnini, Ynini), (Xnfin, Ynfin)]

        return pontos

    # ------------------------------------------------------------------------------------------------------#

    def liang_barsky():
        pass

    # - Sutherland Hodgeman ---------------------------------------------------------------------------------#
    # Retorna o valor x da interseção de dois segmentos de reta
    def sutherland_hodgeman_intersecao_x(x1, y1, x2, y2, x3, y3, x4, y4):
        num = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        return num / den

    # Retorna o valor y da interseção de dois segmentos de reta
    def sutherland_hodgeman_intersecao_y(x1, y1, x2, y2, x3, y3, x4, y4):
        num = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        return num / den

    def sutherland_hodgeman_recortar(pontos_poligono, x1, y1, x2, y2):
        novos_pontos = []
        novo_tamanho_poligono = 0

        # (ix, iy), (kx, ky) são os valores das coordenadas dos pontos
        for i in range(len(pontos_poligono)):
            # i e k formam uma linha no polígono
            k = (i + 1) % len(pontos_poligono)
            ix, iy = pontos_poligono[i]
            kx, ky = pontos_poligono[k]

            # Calculando a posição do primeiro ponto em relação à linha de recorte
            i_pos = (x2 - x1) * (iy - y1) - (y2 - y1) * (ix - x1)

            # Calculando a posição do segundo ponto em relação à linha de recorte
            k_pos = (x2 - x1) * (ky - y1) - (y2 - y1) * (kx - x1)

            # Caso 1: Quando ambos os pontos estão dentro
            if i_pos < 0 and k_pos < 0:
                # Apenas o segundo ponto é adicionado
                novos_pontos.append([kx, ky])
                novo_tamanho_poligono += 1

            # Caso 2: Quando apenas o primeiro ponto está fora
            elif i_pos >= 0 and k_pos < 0:
                # Ponto de interseção com a aresta e o segundo ponto são adicionados
                novos_pontos.append(
                    [
                        Clipping.sutherland_hodgeman_intersecao_x(
                            x1, y1, x2, y2, ix, iy, kx, ky
                        ),
                        Clipping.sutherland_hodgeman_intersecao_y(
                            x1, y1, x2, y2, ix, iy, kx, ky
                        ),
                    ]
                )
                novo_tamanho_poligono += 1
                novos_pontos.append([kx, ky])
                novo_tamanho_poligono += 1

            # Caso 3: Quando apenas o segundo ponto está fora
            elif i_pos < 0 and k_pos >= 0:
                # Apenas o ponto de interseção com a aresta é adicionado
                novos_pontos.append(
                    [
                        Clipping.sutherland_hodgeman_intersecao_x(
                            x1, y1, x2, y2, ix, iy, kx, ky
                        ),
                        Clipping.sutherland_hodgeman_intersecao_y(
                            x1, y1, x2, y2, ix, iy, kx, ky
                        ),
                    ]
                )
                novo_tamanho_poligono += 1

            # Caso 4: Quando ambos os pontos estão fora, nenhum ponto é adicionado

        # Copiando novos pontos na matriz original e alterando o número de vértices
        pontos_poligono[:] = novos_pontos

    def sutherland_hodgeman(pontos_poligono, pontos_recorte):
        # i e k são dois índices consecutivos
        for i in range(len(pontos_recorte)):
            k = (i + 1) % len(pontos_recorte)
            Clipping.sutherland_hodgeman_recortar(
                pontos_poligono,
                pontos_recorte[i][0],
                pontos_recorte[i][1],
                pontos_recorte[k][0],
                pontos_recorte[k][1],
            )

        return pontos_poligono
