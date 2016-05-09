from random import randint

#Random heusistic
def h0(state):
    count = 0

    '''for i in range(1, 8):
        move = (4,i)
        x, y = move
        while state.board.get((x, y)) == 'X':
            count += 1
            x, y = x+1 , y + 0
            #print "y: %d x: %d count: %d" % (y, x, count)
    '''
    return count

def h1(state):
    def k_in_row(board, move, player, (delta_x, delta_y)):
        if player == 'X':
            enemy = 'O'
        else:
            enemy = 'X'
        x, y = move
        n = 0         #Total
        nBlancos = 0  #Number of spaces
        nEnemy = 0    #Number of enemy's boxes
        nPlayer = 0   #Number of player's boxes
        while (x < 8 and x > 0) and (y< 7 and y>0):
            if(board.get((x, y)) == player):
                nPlayer += 1
                if(nPlayer + nBlancos > 3 or nBlancos > 3):
                    n += 10 * nPlayer
                    nEnemy = 0
                    #nBlancos = 0
            elif (board.get((x, y)) == enemy):
                nEnemy += 1
                n -= 10
                nBlancos = 0
                nPlayer = 0
            else :
                if nBlancos < 4:
                    nBlancos += 1
                    n += 5 * nBlancos
            x, y = x + delta_x, y + delta_y
        x, y = move
        nBlancos = 0
        nPlayer = 0
        nEnemy = 0
        while (x < 8 and x > 0) and (y < 7 and y > 0):
            if (board.get((x, y)) == player):
                nPlayer += 1
                if(nPlayer + nBlancos > 3  or nBlancos > 3):
                    n += 10 * nPlayer
                    nEnemy = 0
                    #nBlancos = 0
            elif (board.get((x, y)) == enemy):
                nEnemy += 1
                n -= 10
                nBlancos = 0
                nPlayer = 0
            else:
                if nBlancos < 4:
                    nBlancos += 1
                    n += 5*nBlancos
            x, y = x - delta_x, y - delta_y
        #n -= 10  # Because we counted move itself twice
        return n

    def legal_moves(state):
        "Legal moves are any square not yet taken."
        return [(x, y) for (x, y) in state.moves
                if y == 1 or (x, y - 1) in state.board]

    if state.utility != 0:
        return state.utility * 10000000

    valor_de_heuristica = 0
    ml = legal_moves(state)
    for i in ml:
        #cambiar aqui
        valor_de_heuristica += k_in_row(state.board, i, state.to_move, (1, 0))
        valor_de_heuristica += k_in_row(state.board, i, state.to_move, (1, 1))
        valor_de_heuristica += k_in_row(state.board, i, state.to_move, (1, -1))
        valor_de_heuristica += k_in_row(state.board, i, state.to_move, (0, 1))
    return valor_de_heuristica
