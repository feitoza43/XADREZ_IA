from src.pieces import Pawn, Rook, Knight, Bishop, Queen, King

VALORES = {
    Pawn: 10, Knight: 30, Bishop: 30,
    Rook: 50, Queen: 90, King: 900
}

def avaliar(grid):
    score = 0
    for row in grid:
        for piece in row:
            if piece:
                v = VALORES[type(piece)]
                score += v if piece.color == "black" else -v
    return score

def todos_movimentos(grid, color):
    moves = []
    for r in range(8):
        for c in range(8):
            piece = grid[r][c]
            if piece and piece.color == color:
                for dest in piece.valid_moves(grid):
                    moves.append(((r, c), dest))
    return moves

def aplicar_movimento(grid, origem, dest):
    import copy
    novo = copy.deepcopy(grid)
    r, c = origem
    dr, dc = dest
    novo[dr][dc] = novo[r][c]
    novo[r][c] = None
    novo[dr][dc].position = dest
    novo[dr][dc].moved = True
    return novo

def minimax(grid, depth, alpha, beta, maximizing):
    if depth == 0:
        return avaliar(grid), None

    color = "black" if maximizing else "white"
    moves = todos_movimentos(grid, color)

    if not moves:
        return avaliar(grid), None

    best_move = None

    if maximizing:
        best = float("-inf")
        for origem, dest in moves:
            novo = aplicar_movimento(grid, origem, dest)
            score, _ = minimax(novo, depth - 1, alpha, beta, False)
            if score > best:
                best = score
                best_move = (origem, dest)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best, best_move
    else:
        best = float("inf")
        for origem, dest in moves:
            novo = aplicar_movimento(grid, origem, dest)
            score, _ = minimax(novo, depth - 1, alpha, beta, True)
            if score < best:
                best = score
                best_move = (origem, dest)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best, best_move

def melhor_jogada(grid, depth=2):
    _, move = minimax(grid, depth, float("-inf"), float("inf"), True)
    return move
