import random
def memoize(f):
    memo = {}
    def helper(state, player):
        pair = tuple(state.board.items())
        if pair not in memo:
            memo[pair] = f(state, player)
        return memo[pair]
    return helper

def h0(state):
    return random.randint(-100, 100)

def h1(state):
    if state.utility != 0:
        if state.to_move is '0':
            return state.utility * 1000 * -1
        else:
            return state.utility * 1000
    return fourInRow(state)

def fourInRow(state):
    legalMoves = legal_moves(state)
    value = 0
    for move in legalMoves:
        value += k_in_row(state.board, move, state.to_move, (0, 1))
        value += k_in_row(state.board, move, state.to_move, (1, 0))
        value += k_in_row(state.board, move, state.to_move, (1, 1))
        value += k_in_row(state.board, move, state.to_move, (1, -1))
    opponentValue = 0
    if state.to_move is 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    for move in legalMoves:
        opponentValue += k_in_row(state.board, move, opponent, (0, 1))
        opponentValue += k_in_row(state.board, move, opponent, (1, 0))
        opponentValue += k_in_row(state.board, move, opponent, (1, 1))
        opponentValue += k_in_row(state.board, move, opponent, (1, -1))
    return value - opponentValue

def legal_moves(state):
    """"Legal moves are any square not yet taken."""
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]

def k_in_row(board, move, player, (delta_x, delta_y)):
    """Return true if there is a line through move on board for player."""
    x, y = move
    if player is 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    # it will start in 3 because it is considered this movement has already been done by the player who is playing
    n = 3
    inRow = 1
    for i in range(1, 4, 1):
        x, y = x + delta_x, y + delta_y
        if board.get((x, y)) is player:
            n += 3
            inRow += 1
        if board.get((x, y)) is None: n += 1
        if board.get((x, y)) is opponent: break
    x, y = move
    for i in range(1, 4, 1):
        x, y = x - delta_x, y - delta_y
        if board.get((x, y)) is player:
            n += 3
            inRow += 1
        if board.get((x, y)) is None: n += 1
        if board.get((x, y)) is opponent: break
    if inRow is 4:
        return n + 5000
    return n
@memoize
def h2(state, player):
    return h1(state)
