import games
from heuristics import *
import cristianHeuristics
import guiseHeuristic
import tamaraHeuristic
#game = games.TicTacToe(h=3,v=3,k=3)

def maquinaVsMaquina(state, player):
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == 'X':
            print "Thinking..."
            move = games.alphabeta_search(state, game, eval_fn=h0, d=d)

            state = game.make_move(move, state)
            player = 'O'
        else:
            print "Thinking..."
            move = games.alphabeta_search(state, game, eval_fn=h0, d=d, player = 'O')

            state = game.make_move(move, state)
            player = 'X'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

def empiezasTu(state, player):
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
            move = games.alphabeta_search(state, game, eval_fn=h0, d=d)

            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

def empiezaMaquina(state, player):
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
            move = games.alphabeta_search(state, game, eval_fn=h0, d=d)

            state = game.make_move(move, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break

game = games.ConnectFour()

state = game.initial

selectDificulty = raw_input("Seleccione la dificultad: f->facil, m->medio, d->dificil")

if selectDificulty == 'f':
    print "facil"
    d = 1
elif selectDificulty == 'm':
    print "medio"
    d = 2
elif selectDificulty == 'd':
    print "dificil"
    d = 4
else:
    d = 4
    print "No ha seleccionado ninguna dificultad, dificil por defecto"

selectPlayer = raw_input("Introduzca 'p' si quieres empezar o introduzca 'm' si quieres que empiece la maquina o 'v' para maquina vs maquina")

if selectPlayer == 'p':
    state.to_move = 'O'
    empiezasTu(state, player = 'O')
elif selectPlayer == 'm':
    empiezaMaquina(state, player = 'X')
elif selectPlayer == 'v':
    maquinaVsMaquina(state, player = 'X')
else:
    print "No ha introducido ningun valor correcto, empieza la maquina"
    empiezaMaquina(state, player='X')
