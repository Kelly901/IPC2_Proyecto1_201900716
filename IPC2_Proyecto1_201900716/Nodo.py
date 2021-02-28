class Nodo:

    #nombre= nombre de cada matriz
    #n= la fila de matriz
    #m= columna de la matriz
    #x= la posicion en x que tendra el numero
    #y= la posicion en y que tendra el numero

    def __init__(self,x,y,numero):
            
            self.x=x
            self.y=y
            self.numero=numero
            self.enlace=None
    