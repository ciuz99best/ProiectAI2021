import pygame
from Agent import Agent


class GameBoard:

    def __init__(self):
        self.table_size = 26
        self.x_init, self.y_init = 30, 50
        self.margin_size = self.table_size / 2
        self.board_size = 19
        self.current_piece = 'b'
        self.winner = None
        self.game_over = False
        self.agent = Agent(1, self.board_size)

        self.board = []
        for i in range(self.board_size):
            self.board.append(list("." * self.board_size))

    def mouse_handler(self, mouse):
        origin_x = self.x_init - self.margin_size
        origin_y = self.y_init - self.margin_size
        size = (self.board_size - 1) * self.table_size + self.margin_size * 2
        poz = mouse.pos
        if origin_x <= poz[0] <= origin_x + size and origin_y <= poz[1] <= origin_y + size:
            if not self.game_over:
                x = poz[0] - origin_x
                y = poz[1] - origin_y
                row = int(y // self.table_size)
                col = int(x // self.table_size)
                if self.place_move(row, col):
                    self.verify_state(row, col)

    def place_move(self, row, col):
        if self.board[row][col] == '.':
            self.board[row][col] = self.current_piece

            if self.current_piece == 'b':
                self.current_piece = 'w'
            else:
                self.current_piece = 'b'

            return True
        return False

    def verify_state(self, row, col):
        pieces_N = self.same_piece_len(row, col, -1, 0)
        pieces_S = self.same_piece_len(row, col, 1, 0)

        pieces_E = self.same_piece_len(row, col, 0, 1)
        pieces_W = self.same_piece_len(row, col, 0, -1)

        pieces_SE = self.same_piece_len(row, col, 1, 1)
        pieces_NW = self.same_piece_len(row, col, -1, -1)

        pieces_NE = self.same_piece_len(row, col, -1, 1)
        pieces_SW = self.same_piece_len(row, col, 1, -1)

        if (pieces_N + pieces_S + 1 >= 5) or (pieces_E + pieces_W + 1 >= 5) or \
                (pieces_SE + pieces_NW + 1 >= 5) or (pieces_NE + pieces_SW + 1 >= 5):
            self.winner = self.board[row][col]
            self.game_over = True

    def same_piece_len(self, r, c, dr, dc):
        current_piece = self.board[r][c]
        rez = 0
        i = 1
        while True:
            row_new = r + dr * i
            col_new = c + dc * i
            if 0 <= row_new < self.board_size and 0 <= col_new < self.board_size:
                if self.board[row_new][col_new] == current_piece:
                    rez += 1
                else:
                    break
            else:
                break
            i += 1
        return rez

    def draw(self, screen):
        table_rect = [int(self.x_init - self.margin_size), int(self.y_init - self.margin_size),
                      int((self.board_size - 1) * self.table_size + self.margin_size * 2),
                      int((self.board_size - 1) * self.table_size + self.margin_size * 2)]
        pygame.draw.rect(screen, (185, 122, 87),
                         table_rect, 0)

        for row in range(self.board_size):
            y = self.y_init + row * self.table_size
            pygame.draw.line(screen, (0, 0, 0), [self.x_init, y],
                             [self.x_init + self.table_size * (self.board_size - 1), y], 2)

        for col in range(self.board_size):
            x = self.x_init + col * self.table_size
            pygame.draw.line(screen, (0, 0, 0), [x, self.y_init],
                             [x, self.y_init + self.table_size * (self.board_size - 1)], 2)

        for row in range(self.board_size):
            for col in range(self.board_size):
                current_piece = self.board[row][col]
                if current_piece != '.':
                    if current_piece == 'b':
                        culoare = (0, 0, 0)
                    else:
                        culoare = (255, 255, 255)

                    x = self.x_init + col * self.table_size
                    y = self.y_init + row * self.table_size
                    pygame.draw.circle(screen, culoare, [x, y], self.table_size // 2)

    def agent_pick(self):
        x, y = self.agent.pick()
        while self.board[x][y] == 'b' or self.board[x][y] == 'w':
            x, y = self.agent.pick()
        return self.place_move(x, y)
