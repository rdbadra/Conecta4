import utils

#memoize
def memoize(f):
    memo = {}
    def helper(state, player):
        pair = tuple(state.board.items())
        if pair not in memo:
            memo[pair] = f(state, player)
        return memo[pair]
    return helper

@memoize
def h0(state, player):
    if state.utility != 0:
        if player == 'X':
            return state.utility * utils.infinity
        else:
            return -state.utility * utils.infinity

    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'
    return h1(state, player) - h1(state, enemy)

def h1(state, jugador):
    def k_in_row(board, move, player, (delta_x, delta_y)):
        if player == 'X':
            enemy = 'O'
        else:
            enemy = 'X'
        x, y = move
        n = 0  # Total
        seguidos = 0
        while (x < 8 and x > 0) and (y < 7 and y > 0):
            if (board.get((x, y)) == player):
                n += 30
                seguidos += 1
            elif (board.get((x, y)) == enemy):
                break
            else:
                n += 10
            x, y = x + delta_x, y + delta_y
        x, y = move
        x, y = x - delta_x, y - delta_y
        while (x < 8 and x > 0) and (y < 7 and y > 0):
            if (board.get((x, y)) == player):
                n += 30
                seguidos += 1
            elif (board.get((x, y)) == enemy):
                break
            else:
                n += 10
            x, y = x - delta_x, y - delta_y
        n -= 60
        if seguidos >= 4:
            return n * 100
        elif seguidos >= 3:
            return n*50
        elif seguidos >= 2:
            return n*25
        elif seguidos >= 1:
            return n
        else:
            return 0

    def legal_moves(state):
        return [(x, y) for (x, y) in state.moves
                if y == 1 or (x, y - 1) in state.board]

    valor_de_heuristica = 0
    ml = legal_moves(state)
    a = 0
    for i in ml:
        valor_de_heuristica += k_in_row(state.board, i, jugador, (1, 0))
        valor_de_heuristica += k_in_row(state.board, i, jugador, (1, 1))
        valor_de_heuristica += k_in_row(state.board, i, jugador, (1, -1))
        valor_de_heuristica += k_in_row(state.board, i, jugador, (0, 1))
    return valor_de_heuristica