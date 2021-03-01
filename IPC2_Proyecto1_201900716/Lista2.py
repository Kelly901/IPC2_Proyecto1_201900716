from Nodo2 import Nodo2
class Lista2:

    def __init__(self):
        
        self.cabeza=None



    #Agregar al fina de la lista

    def insertar_final(self,x,y,numero,binario):  
        nuevo=Nodo2(x,y,numero,binario)
        if self.cabeza==None:
            self.cabeza=nuevo
        else:
            auxiliar=self.cabeza
            while auxiliar.enlace is not None:
                auxiliar=auxiliar.enlace
            auxiliar.enlace=Nodo2(x,y,numero,binario)


    #mostrar
    def imprimir(self):
        temp=self.cabeza
        cont=1
        while temp is not None:
            print(str(cont)+' Posicion en x '+str(temp.x)+' posicion y '+ str(temp.y)+"No. "+str(temp.numero)+" Binario. "+str(temp.binario))
            cont=cont+1
            temp=temp.enlace
        print("->")
        
