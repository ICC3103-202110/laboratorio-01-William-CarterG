class Memorice() :
    """
    Representación del juego Memorice

    """
    n = int(input("Ingrese el número de cartas a jugar :\n"))
    def _init_(self, size = n) :
        "Se crean las condicones iniciales del tablero"

        self.pares = set()
        "Ahora se crea un tablero vacío. Por temas de orden cada fila va a tener un máximo arbitrario de 6 cartas"
        self.width  = 6  

        "Para saber cuántas filas crear hay ver si el número n es divisible por 6"
        if n/6 == int(n/6) :
            self.height = n/6
        else :
            self.height = int(n/6) + 1

        self.board = []
        for i range(self.height):
            row = []


        


