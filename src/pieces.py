class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.moved = False

    def opponent(self):
        return "black" if self.color == "white" else "white"

    def in_bounds(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def slide(self, grid, directions):
        moves = []
        r, c = self.position
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while self.in_bounds(nr, nc):
                target = grid[nr][nc]
                if target:
                    if target.color == self.opponent():
                        moves.append((nr, nc))
                    break
                moves.append((nr, nc))
                nr += dr
                nc += dc
        return moves


class Pawn(Piece):
    def valid_moves(self, grid):
        moves = []
        r, c = self.position
        d = -1 if self.color == "white" else 1

        if self.in_bounds(r + d, c) and not grid[r + d][c]:
            moves.append((r + d, c))
            if not self.moved and not grid[r + 2 * d][c]:
                moves.append((r + 2 * d, c))

        for dc in [-1, 1]:
            nr, nc = r + d, c + dc
            if self.in_bounds(nr, nc) and grid[nr][nc] and grid[nr][nc].color == self.opponent():
                moves.append((nr, nc))

        return moves


class Rook(Piece):
    def valid_moves(self, grid):
        return self.slide(grid, [(1,0),(-1,0),(0,1),(0,-1)])


class Bishop(Piece):
    def valid_moves(self, grid):
        return self.slide(grid, [(1,1),(1,-1),(-1,1),(-1,-1)])


class Queen(Piece):
    def valid_moves(self, grid):
        return self.slide(grid, [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)])


class Knight(Piece):
    def valid_moves(self, grid):
        r, c = self.position
        moves = [(r+dr, c+dc) for dr, dc in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]]
        return [(nr, nc) for nr, nc in moves if self.in_bounds(nr, nc) and (not grid[nr][nc] or grid[nr][nc].color == self.opponent())]


class King(Piece):
    def valid_moves(self, grid):
        r, c = self.position
        moves = [(r+dr, c+dc) for dr in [-1,0,1] for dc in [-1,0,1] if (dr, dc) != (0, 0)]
        return [(nr, nc) for nr, nc in moves if self.in_bounds(nr, nc) and (not grid[nr][nc] or grid[nr][nc].color == self.opponent())]