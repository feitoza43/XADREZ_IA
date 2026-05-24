import pygame

LIGHT     = (240, 217, 181)
DARK      = (181, 136, 99)
HIGHLIGHT = (186, 202, 68)
SELECTED  = (246, 246, 105)

SYMBOLS = {
    "Pawn":   {"white": "♙", "black": "♟"},
    "Rook":   {"white": "♖", "black": "♜"},
    "Knight": {"white": "♘", "black": "♞"},
    "Bishop": {"white": "♗", "black": "♝"},
    "Queen":  {"white": "♕", "black": "♛"},
    "King":   {"white": "♔", "black": "♚"},
}

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.size = screen.get_width() // 8
        fonts = ["segoeuisymbol", "segoeui", "dejavusans", "freesans", None]
        self.font = None
        for f in fonts:
            try:
                self.font = pygame.font.SysFont(f, self.size - 8)
                if self.font:
                    break
            except:
                continue

    def draw(self, board, selected):
        moves = []
        if selected:
            piece = board.get(*selected)
            if piece:
                moves = piece.valid_moves(board.grid)

        for row in range(8):
            for col in range(8):
                self._draw_square(row, col, selected, moves)
                piece = board.get(row, col)
                if piece:
                    self._draw_piece(piece, row, col)

    def _draw_square(self, row, col, selected, moves):
        color = LIGHT if (row + col) % 2 == 0 else DARK
        if selected == (row, col):
            color = SELECTED
        elif (row, col) in moves:
            color = HIGHLIGHT
        pygame.draw.rect(self.screen, color, (col * self.size, row * self.size, self.size, self.size))

    def _draw_piece(self, piece, row, col):
        name = type(piece).__name__
        symbol = SYMBOLS[name][piece.color]
        surface = self.font.render(symbol, True, (20, 20, 20))
        x = col * self.size + (self.size - surface.get_width()) // 2
        y = row * self.size + (self.size - surface.get_height()) // 2
        self.screen.blit(surface, (x, y))