import numpy as np


class Clipping:
    @staticmethod
    def point_clippig(Xnponto, Ynponto, Xwmin, Xwmax, Ywmin, Ywmax) -> bool:
        if (Xwmin <= Xnponto <= Xwmax) and (Ywmin <= Ynponto <= Ywmax):
            return True
        return False

    # Cohen Sutherland ----------------------------------------------------------------------------------#
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

    # ----------------------------------------------------------------------------------------------------#

    def liang_barsky():
        pass

    def sutherland_hodgeman():
        pass
