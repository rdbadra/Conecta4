import utils

def memoize(f):
    memo = {}
    def helper(state):
        pair = tuple(state.board.items())
        if pair not in memo:
            memo[pair] = f(state)
        return memo[pair]
    return helper


def legal_moves(state):
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
@memoize
def h1(state):
    if state.utility != 0:
        return utils.infinity*state.utility
    # Legal moves te da los movimientos posibles para ese tablero
    movimientos = legal_moves(state)
    n = 0
    tablero = state.board.copy()

    for move in movimientos:
        n += cuenta_fichas(tablero, move, 'X',(0,1))
        n += cuenta_fichas(tablero, move, 'X', (1,0))
        n += cuenta_fichas(tablero, move, 'X', (1,-1))
        n += cuenta_fichas(tablero, move, 'X', (1,1))

        n -= cuenta_fichas(tablero, move, 'O',(0,1))
        n -= cuenta_fichas(tablero, move, 'O', (1,0))
        n -= cuenta_fichas(tablero, move, 'O', (1,-1))
        n -= cuenta_fichas(tablero, move, 'O', (1,1))
    return n

def cuenta_fichas(board, move, player, (delta_x, delta_y)):
    if player == 'X':
        contrario='O'
    else:
        contrario = 'X'

    x, y = move
    puntuacion = 0
    fichas = 0

    while (board.get((x, y)) == player) or (board.get((x, y)) != contrario):
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
        if board.get((x, y)) == player:
            puntuacion += 3
        else:
            puntuacion += 1
        x, y = x + delta_x, y + delta_y
        fichas +=1
    x, y = move
    while (board.get((x, y)) == player) or (board.get((x, y)) != contrario):
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
        if board.get((x, y)) == player:
            puntuacion += 3
        else:
            puntuacion += 1
        x, y = x - delta_x, y - delta_y
        fichas += 1
    # Because we counted move itself twice
    if fichas-1 < 4:
        return 0
    return puntuacion