#!/usr/bin/env python
"""対話式 CLI：黒番 = エンジン、白番 = ユーザー"""
from reversi.bitboard import Position, BIT
from reversi.movegen import make_move
from reversi.search import best_move

START = Position(
    black=(BIT[14] | BIT[21]),  # d4, e3
    white=(BIT[15] | BIT[20]),  # e4, d3
    turn=0,
)

def print_board(pos: Position):
    table = ["." for _ in range(36)]
    for i in range(36):
        if pos.black & BIT[i]:
            table[i] = "B"
        elif pos.white & BIT[i]:
            table[i] = "W"
    for r in range(6):
        print(" ".join(table[r*6:(r+1)*6]))
    print()

def main():
    pos, depth = START, 6
    while pos.empty:
        print_board(pos)
        if pos.turn == 0:
            mv = best_move(pos, depth)
            if mv is None:
                pos.turn = 1  # パス
                continue
            print(f"Engine: {mv}")
        else:
            mv = int(input("Your move (0‑35): "))
        pos = make_move(pos, mv)

if __name__ == "__main__":
    main()