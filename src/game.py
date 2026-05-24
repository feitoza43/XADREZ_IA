import pygame
from src.board import Board
from src.renderer import Renderer
from src.ai import melhor_jogada

class Game:
    WIDTH, HEIGHT = 640, 640

    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Xadrez")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.renderer = Renderer(self.screen)
        self.selected = None
        self.turn = "white"

    def run(self):
        while True:
            self._handle_events()
            self.renderer.draw(self.board, self.selected)
            pygame.display.flip()
            self.clock.tick(60)

            if self.turn == "black":
                self._ia_jogada()

    def _ia_jogada(self):
        move = melhor_jogada(self.board.grid, depth=2)
        if move:
            origem, dest = move
            self.board.move(origem, dest, "black")
            self.turn = "white"

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.turn == "white":
                self._handle_click(pygame.mouse.get_pos())

    def _handle_click(self, pos):
        col = pos[0] // (self.WIDTH // 8)
        row = pos[1] // (self.HEIGHT // 8)
        row = max(0, min(7, row))
        col = max(0, min(7, col))
        piece = self.board.get(row, col)

        if self.selected:
            if self.selected == (row, col):
                self.selected = None
                return
            moved = self.board.move(self.selected, (row, col), self.turn)
            if moved:
                self.turn = "black"
            self.selected = None
        elif piece and piece.color == self.turn:
            self.selected = (row, col)
