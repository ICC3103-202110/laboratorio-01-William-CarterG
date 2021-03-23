import random

"""
Crea un tablero del juego Memorice

"""
def Board() :
    cards = int(input("Ingrese el número de cartas a jugar :\n"))

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
def printb(board) :
    height = len(board)
    width = 6    #Definí que siempre será igual. De todas maneras se podría hacer para un caso general (pero en este lab nunca habrá otro caso)
    for i in range(height):
        print("-" * width * 9 + "-") # "-" por cada cuadro (cada uno tiene 9 caractéres)
        for j in range(width):
            if board[i][j] != "":
                print("|*(%d, %d)*"%(i, j), end="")
            else:
                print("|        ", end="")
        print("|")
    print("--" * width + "-")

board = Board()
printb(board)

    


