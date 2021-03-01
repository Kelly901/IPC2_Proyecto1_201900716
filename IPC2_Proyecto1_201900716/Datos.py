import xml.etree.ElementTree as ET 
from Lista_simple import Lista
from Matriz import ListaM

class Datos:
   

    def procesar(self,ruta1):
        #ruta=r'C:\Users\Kelly\Desktop\ProyectoIpc2\IPC2_Proyecto1_201900716\prueba.xml'
        ruta=r''+ruta1
        tree=ET.parse(ruta)
        root=tree.getroot()
        cont=0
        
        lista= ListaM()
        
        for element in root:
            
            listaAdentro=Lista()
            
            for i in element:
                listaAdentro.insertar_final(i.attrib['x'],i.attrib['y'],i.text)
                #print(i.attrib['x']+" "+i.attrib['y']+" "+i.text)
            lista.insertar_final(element.attrib['nombre'],element.attrib['n'],element.attrib['m'],listaAdentro)
                   
            cont=cont+1
        #lista.imprimir()   

        
        print("_________________")
        lista.obtener()
        #
        
        '''for element in root:
            lista.insertar_final(element.attrib['nombre'],element.attrib['n'],element.attrib['m'])
        lista.imprimir()'''

