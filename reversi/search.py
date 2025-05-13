from __future__ import annotations
from .movegen import make_move
from .bitboard import Position

INF = 10_000

# 暫定評価
def evaluate(pos: Position) -> int:
    diff = pos.black.bit_count() - pos.white.bit_count()
    return diff * 10 if pos.turn == 0 else -diff * 10

# αβ探索（negamax）
def alphabeta(pos: Position, depth: int, alpha: int, beta: int) -> int:
    if depth == 0 or pos.empty == 0:
        return evaluate(pos)
    moves = pos.legal_moves()
    if not moves:  # パス
        return -alphabeta(Position(pos.black, pos.white, 1 - pos.turn), depth - 1, -beta, -alpha)
    for mv in moves:
        score = -alphabeta(make_move(pos, mv), depth - 1, -beta, -alpha)
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    return alpha

def best_move(pos: Position, depth: int) -> int | None:
    best, alpha = None, -INF
    for mv in pos.legal_moves():
        score = -alphabeta(make_move(pos, mv), depth - 1, -INF, -alpha)
        if score > alpha:
            alpha, best = score, mv
    return best