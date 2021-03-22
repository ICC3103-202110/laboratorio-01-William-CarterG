import random
class Memorice() :
    """
    Representación del juego Memorice

    """
cartas = int(input("Ingrese el número de cartas a jugar :\n"))
    def _init_(self, cartas) :
        #Se crea un tablero vacío. Por temas de orden cada fila va a tener un máximo arbitrario de 6 cartas
        self.width  = 6  

        #Para saber cuántas filas crear hay ver si el número n es divisible por 6
        if cartas/6 == int(cartas/6) :
            self.height = int(2*cartas/6)
        else :
            self.height = int(2*cartas/6) + 1

        #Ahora crearé el tablero y le agregaré las cartas de forma aleatoria 
        c = []
        for i in range(cartas) :
            c.append(i+1)
            c.append(i+1)  

        self.board = []
        for i in range(self.height) :
            row = []
            for j in range(self.width) :
                if len(c) > 0 :
                    x = random.choice(c)
                    c.remove(x)
                    row.append(x)
                else :
                    row.append("")   #Esta condición es necesaria, pues las cartas no tienen porque utilizar todo el tablero, pues este fue creado con tamaños arbitrarios
            self.board.append(row)

    def print(self) :
        



        


