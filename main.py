import pygame
from GameBoard import GameBoard


class Gomoku:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(r"C:\Windows\Fonts\consola.ttf", 24)
        self.going = True
        self.gameboard = GameBoard()

    def loop(self):
        while self.going:
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        for event in pygame.event.get():
            if self.gameboard.current_piece == 'w':
                while not self.gameboard.agent_pick():
                    continue
                continue
            if event.type == pygame.QUIT:
                self.going = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.gameboard.mouse_handler(event)

    def draw(self):
        self.screen.fill((255, 255, 255))

        self.gameboard.draw(self.screen)
        if self.gameboard.game_over:
            self.screen.blit(
                self.font.render("{0} Win".format("Black" if self.gameboard.winner == 'b' else "White"), True,
                                 (0, 0, 0)), (500, 10))

        pygame.display.update()


if __name__ == '__main__':
    game = Gomoku()
    game.loop()
