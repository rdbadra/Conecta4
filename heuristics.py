from random import randint

#Random heusistic
def memoize(f):
    memo = {}
    def helper(x, y , j, k):
        if x not in memo:
            memo[x] = f(x, y, j, k)
        return memo[x]
    return helper

def h0(state):
    if state.to_move == 'X':
        enemy = 'O'
    else:
        enemy = 'X'
    return h1(state, state.to_move) - h1(state, enemy)

def h1(state, player):

    def k_in_row(board, move, player, (delta_x, delta_y)):
        if player == 'X':
            enemy = 'O'
        else:
            enemy = 'X'
        x, y = move
        n = 0         #Total
        nBlancos = 0  #Number of spaces
        nPlayer = 0   #Number of player's boxes
        while (x < 8 and x > 0) and (y< 7 and y>0):
            if(board.get((x, y)) == player):
                nPlayer += 1
                if(nPlayer + nBlancos > 3 or nBlancos > 3):
                    n += 10 * (nPlayer+nBlancos)
            elif (board.get((x, y)) == enemy):
                n -= 10
                nBlancos = 0
                nPlayer = 0
            else :
                if nBlancos < 4:
                    nBlancos += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        nBlancos = 0
        nPlayer = 0
        while (x < 8 and x > 0) and (y < 7 and y > 0):
            if (board.get((x, y)) == player):
                nPlayer += 1
                if(nPlayer + nBlancos > 3  or nBlancos > 3):
                    n += 10 * (nPlayer+nBlancos)
            elif (board.get((x, y)) == enemy):
                n -= 10
                nBlancos = 0
                nPlayer = 0
            else:
                if nBlancos < 4:
                    nBlancos += 1
            x, y = x - delta_x, y - delta_y
        n -= 10  # Because we counted move itself twice
        return n

    def legal_moves(state):
        "Legal moves are any square not yet taken."
        return [(x, y) for (x, y) in state.moves
                if y == 1 or (x, y - 1) in state.board]

    #if state.utility != 0:
     #   return state.utility * 10000000


    def k_in_rowO(board, move, player, (delta_x, delta_y)):
        "Return true if there is a line through move on board for player."

        x, y = move
        n = 1  # n is number of moves in row
        x, y = x + delta_x, y + delta_y
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        x, y = x - delta_x, y - delta_y
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        if n >= 4:

            return 1000000

        else:
            return 0

    '''def k_in_rowX(board, move, player, (delta_x, delta_y)):
        "Return true if there is a line through move on board for player."

        x, y = move
        n = 1  # n is number of moves in row
        x, y = x + delta_x, y + delta_y
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        x, y = x - delta_x, y - delta_y
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        #n -= 1  # Because we counted move itself twic
        if n >= 4:

            if player=='X':
                return 1000000
            else:
                return -1000000
        else:
            return 0'''


    valor_de_heuristica = 0
    valor_de_heuristicaOtro = 0
    ml = legal_moves(state)
    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'
    a = 0
    for i in ml:

        a += k_in_rowO(state.board, i, player, (1, 0))
        a += k_in_rowO(state.board, i, player, (1, 1))
        a += k_in_rowO(state.board, i, player, (1, -1))
        a += k_in_rowO(state.board, i, player, (0, 1))


        if(a!=0):
            return a

        valor_de_heuristica += k_in_row(state.board, i, player, (1, 0))
        valor_de_heuristica += k_in_row(state.board, i, player, (1, 1))
        valor_de_heuristica += k_in_row(state.board, i, player, (1, -1))
        valor_de_heuristica += k_in_row(state.board, i, player, (0, 1))
        '''valor_de_heuristicaOtro += k_in_row(state.board, i, enemy, (1, 0))
        valor_de_heuristicaOtro += k_in_row(state.board, i, enemy, (1, 1))
        valor_de_heuristicaOtro += k_in_row(state.board, i, enemy, (1, -1))
        valor_de_heuristicaOtro += k_in_row(state.board, i, enemy, (0, 1))'''

    return valor_de_heuristica
