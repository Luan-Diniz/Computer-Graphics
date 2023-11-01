import numpy as np


class Clipping:
    # --- Clipping de Pontos ------------------------------------------------------------------------------- #
    @staticmethod
    def point_clippig(Xnponto, Ynponto, Xwmin, Xwmax, Ywmin, Ywmax) -> bool:
        if (Xwmin <= Xnponto <= Xwmax) and (Ywmin <= Ynponto <= Ywmax):
            return True
        return False

    # ------------------------------------------------------------------------------------------------------ #

    # --- Cohen-Sutherland --------------------------------------------------------------------------------- #
    @staticmethod
    def cohen_sutherland_calcular_codigo(X, Y, Xwmin, Xwmax, Ywmin, Ywmax):
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
            if codigo1 == DENTRO and codigo2 == DENTRO:
                aceitar = True
                break
            elif (codigo1 & codigo2) != DENTRO:
                break
            else:
                X = 1.0
                Y = 1.0
                if codigo1 != DENTRO:
                    codigo_fora = codigo1
                else:
                    codigo_fora = codigo2

                if codigo_fora & ACIMA:
                    X = Xnini + (Xnfin - Xnini) * (Ywmax - Ynini) / (Ynfin - Ynini)
                    Y = Ywmax
                elif codigo_fora & ABAIXO:
                    X = Xnini + (Xnfin - Xnini) * (Ywmin - Ynini) / (Ynfin - Ynini)
                    Y = Ywmin
                elif codigo_fora & DIREITA:
                    Y = Ynini + (Ynfin - Ynini) * (Xwmax - Xnini) / (Xnfin - Xnini)
                    X = Xwmax
                elif codigo_fora & ESQUERDA:
                    Y = Ynini + (Ynfin - Ynini) * (Xwmin - Xnini) / (Xnfin - Xnini)
                    X = Xwmin

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

    # ------------------------------------------------------------------------------------------------------ #

    # --- Liang-Barsky ------------------------------------------------------------------------------------- #
    @staticmethod
    def liang_barsky(Xnini, Ynini, Xnfin, Ynfin, Xwmin, Xwmax, Ywmin, Ywmax):
        p1 = -(Xnfin - Xnini)
        p2 = -p1
        p3 = -(Ynfin - Ynini)
        p4 = -p3

        q1 = Xnini - Xwmin
        q2 = Xwmax - Xnini
        q3 = Ynini - Ywmin
        q4 = Ywmax - Ynini

        pk = list(zip([p1, p2, p3, p4], [q1, q2, q3, q4]))
        fora = any([p == 0 and q < 0 for (p, q) in pk])
        if fora:
            return []

        r_negativo = [(q / p) for (p, q) in pk if p < 0]
        u1 = max(0, max(r_negativo, default=0))

        r_positivo = [(q / p) for (p, q) in pk if p > 0]
        u2 = min(1, min(r_positivo, default=1))

        if u1 > u2:
            return []

        novo_Xnini = Xnini + u1 * p2
        novo_Ynini = Ynini + u1 * p4
        novo_Xnfin = Xnini + u2 * p2
        novo_Ynfin = Ynini + u2 * p4

        return [(novo_Xnini, novo_Ynini), (novo_Xnfin, novo_Ynfin)]

    # --- Sutherland-Hodgeman ------------------------------------------------------------------------------ #
    def sutherland_hodgeman_intersecao_x(x1, y1, x2, y2, x3, y3, x4, y4):
        num = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        return num / den

    def sutherland_hodgeman_intersecao_y(x1, y1, x2, y2, x3, y3, x4, y4):
        num = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        return num / den

    def sutherland_hodgeman_recortar(pontos_poligono, x1, y1, x2, y2):
        novos_pontos = []
        novo_tamanho_poligono = 0

        for i in range(len(pontos_poligono)):
            k = (i + 1) % len(pontos_poligono)
            try:
                ix, iy, z = pontos_poligono[i]
                kx, ky, z = pontos_poligono[k]
            except Exception:
                ix, iy= pontos_poligono[i]
                kx, ky= pontos_poligono[k]

            i_pos = (x2 - x1) * (iy - y1) - (y2 - y1) * (ix - x1)
            k_pos = (x2 - x1) * (ky - y1) - (y2 - y1) * (kx - x1)

            if i_pos < 0 and k_pos < 0:
                novos_pontos.append([kx, ky])
                novo_tamanho_poligono += 1

            elif i_pos >= 0 and k_pos < 0:
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

            elif i_pos < 0 and k_pos >= 0:
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

        pontos_poligono[:] = novos_pontos

    def sutherland_hodgeman(pontos_poligono, pontos_recorte):
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

    # ------------------------------------------------------------------------------------------------------ #
