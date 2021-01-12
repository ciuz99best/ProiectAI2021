import pygame


class TablaJoc:

    def __init__(self):
        self.dimensiune_retea = 26
        self.x_initial, self.y_initial = 30, 50
        self.dim_muchie = self.dimensiune_retea / 2
        self.dimensiune_tabla = 19
        self.piesa = 'b'
        self.castigator = None
        self.game_over = False

        self.retea = []
        for i in range(self.dimensiune_tabla):
            self.retea.append(list("." * self.dimensiune_tabla))

    def handle_eveniment(self, eveniment):
        origin_x = self.x_initial - self.dim_muchie
        origin_y = self.y_initial - self.dim_muchie
        size = (self.dimensiune_tabla - 1) * self.dimensiune_retea + self.dim_muchie * 2
        poz = eveniment.pos
        if origin_x <= poz[0] <= origin_x + size and origin_y <= poz[1] <= origin_y + size:
            if not self.game_over:
                x = poz[0] - origin_x
                y = poz[1] - origin_y
                rand = int(y // self.dimensiune_retea)
                col = int(x // self.dimensiune_retea)
                if self.seteaza_piesa(rand, col):
                    self.finalizare_joc(rand, col)


    def seteaza_piesa(self, rand, col):
        if self.retea[rand][col] == '.':
            self.retea[rand][col] = self.piesa

            if self.piesa == 'b':
                self.piesa = 'w'
            else:
                self.piesa = 'b'

            return True
        return False

    def finalizare_joc(self, rand, col):
        coordonate_N = self.preia_coordonate(rand, col, -1, 0)
        coordonate_S = self.preia_coordonate(rand, col, 1, 0)

        coordonate_E = self.preia_coordonate(rand, col, 0, 1)
        coordonate_V = self.preia_coordonate(rand, col, 0, -1)

        coordonate_SE = self.preia_coordonate(rand, col, 1, 1)
        coordonate_NV= self.preia_coordonate(rand, col, -1, -1)

        coordonate_NE = self.preia_coordonate(rand, col, -1, 1)
        coordonate_SV = self.preia_coordonate(rand, col, 1, -1)

        if (coordonate_N + coordonate_S + 1 >= 5) or (coordonate_E + coordonate_V + 1 >= 5) or \
                (coordonate_SE + coordonate_NV + 1 >= 5) or (coordonate_NE + coordonate_SV + 1 >= 5):
            self.castigator = self.retea[rand][col]
            self.game_over = True

    def preia_coordonate(self, r, c, dr, dc):
        piesa = self.retea[r][c]
        rez = 0
        i = 1
        while True:
            rand_nou = r + dr * i
            col_noua = c + dc * i
            if 0 <= rand_nou < self.dimensiune_tabla and 0 <= col_noua < self.dimensiune_tabla:
                if self.retea[rand_nou][col_noua] == piesa:
                    rez += 1
                else:
                    break
            else:
                break
            i += 1
        return rez

    def draw(self, screen):
        pygame.draw.rect(screen, (185, 122, 87),
                         [self.x_initial - self.dim_muchie, self.y_initial - self.dim_muchie,
                          (self.dimensiune_tabla - 1) * self.dimensiune_retea + self.dim_muchie * 2, (self.dimensiune_tabla - 1) * self.dimensiune_retea + self.dim_muchie * 2], 0)

        for rand in range(self.dimensiune_tabla):
            y = self.y_initial + rand * self.dimensiune_retea
            pygame.draw.line(screen, (0, 0, 0), [self.x_initial, y], [self.x_initial + self.dimensiune_retea * (self.dimensiune_tabla - 1), y], 2)

        for col in range(self.dimensiune_tabla):
            x = self.x_initial + col * self.dimensiune_retea
            pygame.draw.line(screen, (0, 0, 0), [x, self.y_initial], [x, self.y_initial + self.dimensiune_retea * (self.dimensiune_tabla - 1)], 2)

        for rand in range(self.dimensiune_tabla):
            for col in range(self.dimensiune_tabla):
                piesa = self.retea[rand][col]
                if piesa != '.':
                    if piesa == 'b':
                        culoare = (0, 0, 0)
                    else:
                        culoare = (255, 255, 255)

                    x = self.x_initial + col * self.dimensiune_retea
                    y = self.y_initial + rand * self.dimensiune_retea
                    pygame.draw.circle(screen, culoare, [x, y], self.dimensiune_retea // 2)