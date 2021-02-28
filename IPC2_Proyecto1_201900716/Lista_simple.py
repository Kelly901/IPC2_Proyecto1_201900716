from Nodo import Nodo
class Lista:

    def __init__(self):
        
        self.cabeza=None



    #Agregar al fina de la lista

    def insertar_final(self,x,y,numero):  
        nuevo=Nodo(x,y,numero)
        if self.cabeza==None:
            self.cabeza=nuevo
        else:
            auxiliar=self.cabeza
            while auxiliar.enlace is not None:
                auxiliar=auxiliar.enlace
            auxiliar.enlace=Nodo(x,y,numero)


    #mostrar
    def imprimir(self):
        temp=self.cabeza
        cont=1
        while temp is not None:
            print(str(cont)+' Posicion en x '+str(temp.x)+' posicion y '+ str(temp.y)+"No. "+str(temp.numero))
            cont=cont+1
            temp=temp.enlace
        print("->")
        
