import games
from heuristics import *

#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial

selectPlayer = raw_input("Introduzca p si quieres empezar o introduzca m si quieres que empiece la maquina")

if selectPlayer == 'p':
    player = 'O'
    print "Empiezas tu"
else:
    player = 'X'
    print "Empieza la maquina"

selectDificulty = raw_input("Seleccione la dificultad: f->facil, m->medio, d->dificil")

if selectDificulty == 'f':
    d = 1
elif selectDificulty == 'm':
    d = 2
if selectDificulty == 'd':
    d = 4
else:
    d = 4
    print "No ha seleccionado ninguna dificultad"


while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game, eval_fn = h1,d = d)
        #print h1(state)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
