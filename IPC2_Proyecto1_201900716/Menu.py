from Lista_simple import Lista
from Matriz import ListaM
from Datos import Datos
lis=Lista()
matriz=ListaM()
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
            d=Datos()
            d.procesar(self.ruta)
            self.menu()
            
        elif opcion=="2":
            print("Procesar Archivo")
            print(self.ruta)
            print(">Calculando la matriz binaria...")
            print(">Realizando suma de Tuplas...")
            self.menu()
        elif opcion=="3":
            print("Escribir archivo de salida")
            print("____________________________")
            self.menu()
        elif opcion=="4":
            print("Mostrar datos del estudiante")
        elif opcion=="5":
            print("Generar grafica")
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
    
