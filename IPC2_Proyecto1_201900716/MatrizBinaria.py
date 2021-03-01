from NodoB import NodoB
class ListaB:

    def __init__(self):
        self.lista=None
        self.cabeza=None
       
        
    #Agregar al final de la lista

    def insertar_final(self,nombre,n,m,matriz):
        
        nuevo= NodoB(nombre,n,m)
        #lista va a ser la lista que va almacenas los datos
        nuevo.matriz=matriz
        if self.cabeza==None:
            self.cabeza=nuevo
        else:
            auxiliar=self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar=auxiliar.siguiente
            auxiliar.siguiente=nuevo

    def imprimir(self):
        
        
        temp=self.cabeza
        cont=1
        while temp is not None:
            print(str(cont)+'nombre: '+temp.nombre+' fila: '+str(temp.n)+' Columna: '+str(temp.m))  
            temp.matriz.imprimir()
            cont=cont+1
            temp=temp.siguiente 
            

    def imprimirMatriz(self):

        temp=self.cabeza

        while temp is not None:
            
            aux=temp.matriz.cabeza
            if temp.nombre:
                
                print(temp.nombre)    
                for i in range(int(temp.n)):
                    for j in range(int(temp.m)):
                        
                        numero=aux.binario
                    
                        print("\t",numero,end=" ")
                       
                        aux=aux.enlace
                        
                    print()    
            temp=temp.siguiente   


    '''def suma(self):

        temp=self.cabeza
        while temp is not None:

            aux=temp.cabeza

            if temp.nombre:

                for i in range(int(temp.n)):
                    for j in range(int(temp.n)):'''

                        

            