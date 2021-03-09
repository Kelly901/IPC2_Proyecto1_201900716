from Lista_simple import Lista
from Matriz import ListaM
from Datos import Datos
from Lista2 import Lista2
from MatrizBinaria import ListaB
lis=Lista()
list2=Lista2()
listaB=ListaB()
listaM=ListaM()

class Menu:
    ruta=""
    def menu(self):
        print(">>>>>>>>>>Menu Principal<<<<<<<<<<<<")
        print("1.Cargar Archivo")
        print("2.Procesar Archivo")
        print("3.Escribir archivo de salida")
        print("4.Mostrar datos del estudiante")
        print("5.Generar gráfica")
        print("6.Salida")
        opcion= input("Ingrese una opción -->")
        self.opciones(opcion)

    def opciones(self,opcion):
       
        if opcion=="1":
            print("Cargar Archivo")
            print("_______________________")
            self.ruta=input("Ingrese la ruta: ")
            #d=Datos()
            #d.procesar(self.ruta)
            
            self.menu()
            
            
        elif opcion=="2":
            print("Procesar Archivo")
            print(self.ruta)
            print(">Calculando la matriz binaria...")
            print(">Realizando suma de Tuplas...")
            
            print(listaB.imprimirMatriz())
            d=Datos()
            d.procesar(self.ruta)
            print(".......")
           
            self.menu()
        elif opcion=="3":
            print("Escribir archivo de salida")
            print("____________________________")
            
            
            self.menu()
        elif opcion=="4":
            print("________________________________________")
            print("Mostrar datos del estudiante")
            print("Kelly Mischel Herrera Espino \n201900716 \nIntroducción a la Programación y Computación Sección \"D\" \nIngenieria en Ciencias y Sistemas \n4to Semestre")
            self.menu()
        elif opcion=="5":
            print("Generar grafica")
            nombre=input("Ingrese el nombre de la grafia-> ")
            Datos.lista.grafi(nombre)
            self.menu()
        elif opcion=="6":
            print("Salida")
        else:
            print("         ")
            print("------------------------")
            print("La opcion numero "+opcion+" no existe.")  
            print("Vuelva a ingresar otra opcion.")
            print("      ")  
            self.menu()                     

    # Opciones para procesar el archivo
    
