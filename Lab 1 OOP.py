import random

"""
Crea un tablero del juego Memorice

"""
def Board(cards) :
    #Se crea un tablero vacío. Por temas de orden cada fila va a tener un máximo arbitrario de 6 cartas
    width  = 6  

    #Para saber cuántas filas crear hay ver si el número n es divisible por 6
    if cards/6 == int(cards/6) :
        height = int(2*cards/6)
    else :
        height = int(2*cards/6) + 1

    #Ahora crearé el tablero y le agregaré las cartas de forma aleatoria 
    c = []
    for i in range(cards) :
        c.append(i+1)
        c.append(i+1)  

    board = []
    for i in range(height) :
        row = []
        for j in range(width) :
            if len(c) > 0 :
                x = random.choice(c)
                c.remove(x)
                row.append(x)
            else :
                row.append("")   #Esta condición es necesaria, pues las cartas no tienen porque utilizar todo el tablero.
        board.append(row)
    return board


"""
Imprime las condiciones del tablero actual 
"""
def printb(board, found) :
    #Esta fue la forma más simple que se me ocurrio de como imprimir cualquier carta :(
    for i in range(height) :
        for j in range(width) :
        for pair in found :
            if (i,j)==(pair[0],pair[1]):
                board[i][j] = str(board[i][j])          

    height = len(board)
    width = 6    #Definí que siempre será igual. De todas maneras se podría hacer para un caso general (pero en este lab nunca habrá otro caso)
    for i in range(height):
        print("-" * width * 9 + "-") # "-" por cada cuadro (width) por el espacio que ocupan (cada uno tiene 9 caractéres)
        for j in range(width):
            if isinstance(board[i][j],str) :  #Si es str, se va a imprimir el número (a menos que sea "", porque defimí que esas son las cartas que se deben ver)
                if board[i][j] != "":
                    print("|   %s    "%board[i][j], end="")
                else:
                    print("|        ", end="")
            else : #Cómo no son str, sólo mostraré la coordenada en que se encuentran
                print("|*(%d, %d)*"%(i, j), end="")
        print("|")
    print("--" * width + "-")

def Memorice(board, found) :
    val = 0 #validity of coordinates
    while val == 0 :
        coor1 = input("Ingresa las coordenadas de la primera carta (i,j) :\n")
        coor1_x , coor1_y = coor1[1], coor1[-2]

        #Sólo por las dudas, voy a validar que las coordenadas estén bien (la ayudante nos dijo que era siempre
        # recomendable). Perdón por la línea gigante:( Pero son muchas condiciones que hay que comprobar...
        if (0 <= (int(coor1_x) and int(coor1_y)))
        and int(coor1_x) < len(board) and int(coor1_y) < 6 
        and (coor1[1].isnumeric() and coor1[-2].isnumeric()) == True :

            c_1  = int(coor1_x), int(coor1_y)
            found.append(c_1)
            printb(board, found)
            val = 1

    val = 0
    while val == 0 :
        coor2 = input("Ingresa las coordenadas de la segunda carta (i,j) :\n")
        coor2_x , coor2_y = coor2[1], coor2[-2]

        #Perdón... denuevo  :(
        if (0 <= (int(coor2_x) and int(coor2_y))) 
        and int(coor2_x) < len(board) and int(coor2_y) < 6 
        and (coor2[1].isnumeric() and coor2[-2].isnumeric()) == True :
            c_2 = int(coor2_x), int(coor2_y)
            found.append(c_2)
            printb(board, found)
            val = 1

    return c_1, c_2
    
def Interfaz():
    print("¡Bienvenido a Memorice!\n")
    juego = 1 # int(input("Ingresa 1 en la terminal para jugar!!. Si deseas dalir, ingresa 0"))
    while juego != 0 :
        print("""***INSTRUCCIONES***\nEn este juego habrán una cierta cantidad de pares de cartas iguales, pero estas estarán
desordenadas y ocultas en el tablero.\nDos jugadores se turnarán para tratar de encontrar los pares de cartas iguales,
eligiendo 2 cartas en cada turno. Si las cartas elegidas son iguales, el jugador que las
eligió sumará un punto y repetirá su turno. Si no, es turno del otro\nEl juego termina cuando encuentren todos
los pares\n ¡¡¡Buena suerte!!!""")

        cards = int(input("Ingrese el número de cartas a jugar :\n"))
        board = Boards(cards)
        p_1, p_2 = 0, 0
        
        turn = 0
        found  = []
        while len(found) != 2*cards
            while (turn/2) == int(turn/2) :
               c_1, c_2 = Memorice(board)




