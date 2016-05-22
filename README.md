# Conecta-4
Práctica para la asignatura de fundamentos de los sistemas inteligentes que implementa
el juego Conecta-4.
Para el funcionamiento de esta práctica, se han modificado los siguientes ficheros:

* heuristics.py
* run.py
* games.py

Además se han incluido tres heurísticas diferentes para poner a prueba nuestra heurística.

### heuristics.py
En este fichero se ha implementado la heurística que usa la máquina cuando juega.
En ella se tienen en cuenta los siguientes aspectos:

1. Se comprueba si el jugador está en un estado ganador o perdedor, en cuyo caso devolverá inf o -inf respectivamente.
2. Cada posición en donde haya una ficha del jugador actual suma 30.
3. Cuando encuentra una pieza del jugador contrario deja de sumar.
4. Al final se resta 60 porque se cuentan dos posiciones repetidas.
5. Una vez haya terminado de comprobar todos los movimientos, comprueba cuantas seguidas hay del mismo jugador:

    * Si hay 4 o más seguidas se multiplica por 100
    * Si hay 3 seguidas se multiplica por 50
    * Si hay 2 seguidas se multiplica por 25
    * Si hay 1 no se multiplica por nada

6. Si no se encuentra en un estado ganador se devuelve la resta de la heurística del jugador actual menos la del enemigo, teniendo en cuenta todos los aspectos anteriores.

### run.py
Aquí se ha definido el nivel de dificultad de la partida y la decisión de quién empieza a jugar.
Con respecto a la dificultad se puede elegir entre tres tipos:
Fácil, medio y difícil. Cuanto más dificil sea la partida, más movimientos podrá simular la máquina ya que
hay más niveles de profundidad. En la elección de jugador, podemos elegir si empezamos a poner fichas nosotros o la máquina. Además podemos escoger la opción de poner
a jugar dos heurísticas iguales o diferentes.

### games.py
Por último, se ha modificado la función alphabeta_search, en concreto la función de evaluación, para que reciba el estado y el jugador.
