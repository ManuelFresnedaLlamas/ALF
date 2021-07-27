'''
Created on 21 jun. 2020

@autores: David Martinez Pozuelo, Manuel Fresneda Llamas
'''

from jflap.Afd import Afd
from nt import listdir
import sys

ruta = r'C:\Users\USUARIO\Desktop\PracticasAlf\automata.jff'
    
def getFichero():
    
    print('Introduzca el nombre del fichero')
    archivo=input()
    return archivo    

def abrirFichero(archivo):
    if(len(archivo))==0:
        sys.exit()
        
    listaArchivos=listdir(".")
    
    for i in listaArchivos:
        if(i==archivo):
            return True
        
    return False
    
    
def stringValida(string):
    
    global contador
    contador=0
    
    simboloAlfabeto=None #Declaramos la variable simbolo
    
    estadoActual=automataDet.getEstadoInicial()

    while contador < len(string) - 2: #Recorremos la senal binaria recibida de 2 en 2
        
        simboloAlfabeto=string[contador] + string[contador + 1] #Guardamos el par a estudiar
        
        if (automataDet.estadoSiguiente(estadoActual,simboloAlfabeto)):
            
            estadoActual=automataDet.estadoSiguiente(estadoActual,simboloAlfabeto)
            contador=contador + 2
            
        else:
            contador=contador + 2
            return False
        
    return True

if __name__ == '__main__':
    
    posicionLinea=1 #usaremos para indicar la linea
    
    automataDet=Afd(ruta)
    
    fichero=False
    global contador
    
    while fichero==False:
        archivo=getFichero()
        fichero=abrirFichero(archivo)   
        
        if fichero==False:
            print('El fichero no existe') 
            
    archivoOpen=open(archivo)
    
    while True:
        linea=archivoOpen.readline() #lista de todas las lineas
        
        string=linea.rstrip('\n') #indicamos separador
        
        if stringValida(string): #llamamos a la funcion
            
            if len(string)==0:
                break
            
            print('Linea',posicionLinea,string,': valida')
            
            posicionLinea=posicionLinea+1
            
        else:
            
            if len(string)==0:
                break
            
            print('Linea',posicionLinea,string,': no es valida en ',contador)
            
            posicionLinea=posicionLinea+1
            
            