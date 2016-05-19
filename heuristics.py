import utils

#memoize
def memoize(f):
    memo = {}
    def helper(state):
        pair = tuple(state.board.items())
        if pair not in memo:
            memo[pair] = f(state)
        return memo[pair]
    return helper

# Random heusistic
@memoize
def h0(state):
    if state.utility != 0:
        if state.to_move == 'X':
            return state.utility * utils.infinity
        else:
            return state.utility * -utils.infinity
    if state.to_move == 'X':
        enemy = 'O'
    else:
        enemy = 'X'
    return h1(state, state.to_move) - h1(state, enemy)

def h1(state, jugador):
    def k_in_row(board, move, player, (delta_x, delta_y)):
        if player == 'X':
            enemy = 'O'
        else:
            enemy = 'X'
        x, y = move
        x, y = x + delta_x, y + delta_y
        n = 10  # Total
        nBlancos = 0  # Number of spaces
        nPlayer = 1  # Number of player's boxes
        while (x < 8 and x > 0) and (y < 7 and y > 0):
            if (board.get((x, y)) == player):
                nPlayer += 1
                if (nPlayer + nBlancos > 3 or nBlancos > 3):
                    n += 10 * nPlayer + 5 * nBlancos
            elif (board.get((x, y)) == enemy):
                n -= 10
                nBlancos = 0
                nPlayer = 0
            else:
                if nBlancos < 4:
                    nBlancos += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        x, y = x - delta_x, y - delta_y
        nBlancos = 0
        nPlayer = 1
        while (x < 8 and x > 0) and (y < 7 and y > 0):
            if (board.get((x, y)) == player):
                nPlayer += 1
                if (nPlayer + nBlancos > 3 or nBlancos > 3):
                    n += 10 * nPlayer + 5 * nBlancos
            elif (board.get((x, y)) == enemy):
                n -= 10
                nBlancos = 0
                nPlayer = 0
            else:
                if nBlancos < 4:
                    nBlancos += 1
            x, y = x - delta_x, y - delta_y
        return n

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
