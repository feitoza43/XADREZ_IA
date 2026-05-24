from src.pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.grid = [[None] * 8 for _ in range(8)]
        self._setup()

    def _setup(self):
        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, Piece in enumerate(order):
            self.grid[0][col] = Piece("black", (0, col))
            self.grid[7][col] = Piece("white", (7, col))
        for col in range(8):
            self.grid[1][col] = Pawn("black", (1, col))
            self.grid[6][col] = Pawn("white", (6, col))

    def get(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.grid[row][col]
        return None

    def move(self, origin, dest, turn):
        row, col = origin
        dr, dc = dest
        piece = self.grid[row][col]

        if not piece:
            print(f"ERRO: sem peça em {origin}")
            return False
        if piece.color != turn:
            print(f"ERRO: peça {piece.color} mas turno {turn}")
            return False

        valid = piece.valid_moves(self.grid)
        print(f"Movimentos válidos de {origin}: {valid}")

        if dest not in valid:
            print(f"ERRO: {dest} não é movimento válido")
            return False

        self.grid[dr][dc] = piece
        self.grid[row][col] = None
        piece.position = dest
        piece.moved = True
        print(f"Movimento OK: {origin} -> {dest}")
        return True
