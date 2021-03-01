from NodoM import NodoM
from Lista_simple import Lista
from MatrizBinaria import ListaB
from Lista2 import Lista2
lis=Lista()
class ListaM:

    def __init__(self):
        self.lista=None
        self.cabeza=None
       
        
    #Agregar al final de la lista

    def insertar_final(self,nombre,n,m,matriz):
        self.lista=matriz
        nuevo= NodoM(nombre,n,m)
        #lista va a ser la lista que va almacenas los datos
        nuevo.matriz=self.lista
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
            

    def obtener(self):

        temp=self.cabeza
        listaB=ListaB()
        while temp is not None:
            aux=temp.matriz.cabeza
            if temp.nombre:
                #print(temp.nombre)
                lista2=Lista2()
                while aux is not None:
                    
                    
                    binario=""
                    
                    if aux.numero=="0":
                        binario=0
                    else:
                        binario=1    
                    lista2.insertar_final(aux.x,aux.y,aux.numero,binario)
                    aux=aux.enlace
                    #print(lista2.imprimir()) 
                    
                listaB.insertar_final(temp.nombre,temp.n,temp.m,lista2)        
                #listaB.imprimir()
                
            temp=temp.siguiente
        listaB.imprimirMatriz()             