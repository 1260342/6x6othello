"""6×6 Reversi bitboard utilities."""
from __future__ import annotations
from dataclasses import dataclass

# マス番号 0..35 = a6..f1（上から下、左から右）
BIT = [1 << i for i in range(36)]
MASK36 = (1 << 36) - 1
DIRECTIONS = (-6, -5, -4, -1, 1, 4, 5, 6)  # N, NE, E, SE, S, SW, W, NW

def shift_bits(bits: int, d: int) -> int:
    return ((bits << d) & MASK36) if d > 0 else (bits >> (-d))

@dataclass(slots=True)
class Position:
    black: int  # 先手
    white: int  # 後手
    turn: int   # 0 = 黒番, 1 = 白番

    @property
    def empty(self) -> int:  # 空点マスク
        return (~(self.black | self.white)) & MASK36

    # 合法手リスト（インデックス配列）
    def legal_moves(self) -> list[int]:
        me, opp = (self.black, self.white) if self.turn == 0 else (self.white, self.black)
        moves = 0
        for d in DIRECTIONS:
            mask = shift_bits(opp, d)
            mask &= MASK36
            mask = shift_bits(mask, d)
            while mask & opp:
                mask = shift_bits(mask, d)
            moves |= mask & self.empty
        return [i for i in range(36) if moves & BIT[i]]