def memoize(f):
    memo = {}
    def helper(state, player):
        pair = tuple(state.board.items())
        if pair not in memo:
            memo[pair] = f(state, player)
        return memo[pair]
    return helper

def PPlayer(state, move, player, (delta_x, delta_y)):
    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'
    n = 0
    seguidos = 0
    x, y = move
    while (x > 0 and x < 8 ) and (y > 0 and y < 7):
        if state.board.get((x, y)) == player:
            n += 6
        elif state.board.get((x, y)) == enemy:
            break
        else:
            n += 2
        x, y = x + delta_x, y + delta_y
        seguidos += 1
    x, y = move
    while (x > 0 and x < 8) and (y > 0 and y < 7):
        if state.board.get((x, y)) == player:
            n += 6
        elif state.board.get((x, y)) == enemy:
            break
        else:
            n += 2
        x, y = x - delta_x, y - delta_y
        seguidos += 1
    n -= 12
    if seguidos >= 4:
        return n
    else:
        return 0
@memoize
def h1(state,player):
    #player = state.to_move
    if player == 'X':
        contrario = 'O'
    else:
        contrario = 'X'

    if state.utility!=0:
        if player == 'X':
            return state.utility * 100000
        else:
            return state.utility * -100000

    def legal_moves(state):
        return [(x, y) for (x, y) in state.moves
                if y == 1 or (x, y - 1) in state.board]

    valor_de_heuristica=0

    l_moves =legal_moves(state)
    for move in l_moves:

        valor_de_heuristica += PPlayer(state, move, player, (1, 0))
        valor_de_heuristica += PPlayer(state, move, player, (0, 1))
        valor_de_heuristica += PPlayer(state, move, player, (1, 1))
        valor_de_heuristica += PPlayer(state, move, player, (1, -1))

        valor_de_heuristica -= PPlayer(state, move, contrario, (1, 0))
        valor_de_heuristica -= PPlayer(state, move, contrario, (0, 1))
        valor_de_heuristica -= PPlayer(state, move, contrario, (1, 1))
        valor_de_heuristica -= PPlayer(state, move, contrario, (1, -1))

        return valor_de_heuristica