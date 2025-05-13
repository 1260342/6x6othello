from .bitboard import Position, BIT, DIRECTIONS, shift_bits

# 着手して次局面を返す
def make_move(pos: Position, sq: int) -> Position:
    me, opp = (pos.black, pos.white) if pos.turn == 0 else (pos.white, pos.black)
    flip = 0
    for d in DIRECTIONS:
        cur = shift_bits(BIT[sq], d)
        line = 0
        while cur & opp:
            line |= cur
            cur = shift_bits(cur, d)
        if cur & me:
            flip |= line
    me ^= flip | BIT[sq]
    opp ^= flip
    if pos.turn == 0:
        return Position(me, opp, 1)
    return Position(opp, me, 0)