'''
Created on 30 jun. 2020

@autores: David Martinez Pozuelo, Manuel Fresneda Llamas
'''
import sys 
import regex as re
from visor import mostrar
import math
from os import listdir

def leerFichero(nombre):
    
    with open(nombre) as fichero:
        
        lineas = (linea.rstrip() for linea in fichero)
        lineas = list(linea for linea in lineas if linea)
    
    valido = True 
    cont = 0
    auxiliar = 0
    
    for i in lineas:
        
        cont += 1
        priLinea = i[0]
        
        if len(i) > 1:
            priLinea = i[0] + i[1]
        
        if not (priLinea == 'v ' or priLinea == 'vn' or priLinea == 'vt' or priLinea == 'f '):
            continue
        
        if priLinea == 'v ':
            resultado = ERV.fullmatch(i)
            
            if resultado:
                listaVertices = [resultado.group('num1'), resultado.group('num2'), resultado.group('num3')]
                V.append(listaVertices)
                
            else:
                valido = False
                print('Hay un error en la linea: ', cont, file = sys.stderr)
                sys.exit()
                
        if priLinea == 'vn' :
            resultado = ERVn.fullmatch(i)
            
            if resultado:
                listaNormales = [resultado.group('num1'), resultado.group('num2'), resultado.group('num3')]
                N.append(listaNormales)
                
            else:
                valido = False
                print('Hay un error en el vector normal: ', cont, file = sys.stderr)
                sys.exit()
                
        if priLinea == 'vt':
            resultado = ERTexturas.fullmatch(i)
            
            if resultado:
                
                if resultado.group('num3')==None:
                    arrayVt = [resultado.group('num1'),resultado.group('num2')]
                    T.append(arrayVt)
                else:
                    arrayVt = [resultado.group('num1'),resultado.group('num2'),resultado.group('num3')]
                    T.append(arrayVt)
                    
            else:
                valido = False
                print('Hay un error en vertice: ',cont, file = sys.stderr)
                
        if priLinea == 'f ' :
            resultado = ERF.fullmatch(i)
            
            if resultado:
                auxi = resultado.group('tri1')
                x = 0
                y = 0
                z = 0
                resultadoAux = ERTripleta.fullmatch(auxi)
                
                if resultadoAux:
                    FV.append(int(resultadoAux.group('n1')) - 1)
                    x = int(resultadoAux.group('n1')) - 1
                
                auxTri2 = resultado.group('tri2')
                resultadoauxTri2 = ERTripleta.fullmatch(auxTri2)
                
                if resultadoauxTri2:
                    FV.append(int(resultadoauxTri2.group('n1')) - 1)
                    y = int(resultadoauxTri2.group('n1')) - 1
            
                auxTri3 = resultado.group('tri3')
                resultadoauxTri3 = ERTripleta.fullmatch(auxTri3)
            
                if resultadoauxTri3 :
                    FV.append(int(resultadoauxTri3.group('n1')) - 1)
                    z = int(resultadoauxTri3.group('n1')) - 1
            
                    auxTri1 = resultado.group('tri1')
                    resultadoauxTri1 = ERTripleta.fullmatch(auxTri1)
                    
                if resultadoauxTri1 : 
                    
                    if resultadoauxTri1.group('n2') != None :
                        FT.append(int(resultadoauxTri1.group('n2')) - 1)
                    
                auxTri2 = resultado.group('tri2')
                resultadoauxTri2 = ERTripleta.fullmatch(auxTri2)
                
                if resultadoauxTri2 : 
                    
                    if resultadoauxTri2.group('n2') != None :
                        FT.append(int(resultadoauxTri2.group('n2')) - 1)
            
                auxTri3 = resultado.group('tri3')
                resultadoauxTri1 = ERTripleta.fullmatch(auxTri1)
                
                if resultadoauxTri1 : 
                    
                    if resultadoauxTri1.group('n2') != None :
                        FT.append(int(resultadoauxTri3.group('n2')) - 1)

                auxi = resultado.group('tri1')
                resultadoAux = ERTripleta.fullmatch(auxi)

                if resultadoAux:
                    
                    if resultadoAux.group('n3') != None:
                        FN.append(int (resultadoAux.group('n3')) - 1)
                        
                    else:
                        vertice1 = V[x]
                        vertice2 = V[y]
                        vertice3 = V[z]
                        X = [float(vertice2[0]) - float(vertice1[0]), float(vertice2[1]) - float(vertice1[1]), float(vertice2[2]) - float(vertice1[2])]
                        Y = [float(vertice3[0]) - float(vertice1[0]), float(vertice3[1]) - float(vertice1[1]), float(vertice3[2]) - float(vertice1[2])]
                        Nauxiliar = [X[1] * Y[2] - X[2] * Y[1], X[2] * Y[0] - X[0] * Y[2], X[0] * Y[1] - X[1] * Y[0]]
                        Nab = math.sqrt((Nauxiliar[0] ** 2) + (Nauxiliar[1] ** 2) + (Nauxiliar[2] ** 2))
                        Ndef = [Nauxiliar[0] / Nab, Nauxiliar[1] / Nab, Nauxiliar[2] / Nab]
                        
                        N.append(Ndef)
                        FN.append(auxiliar)
                        FN.append(auxiliar)
                        FN.append(auxiliar)
                        auxiliar = auxiliar + 1

                auxi2 = resultado.group('tri3')
                resultadoAuxi2 = ERTripleta.fullmatch(auxi2)
                
                if resultadoAuxi2.group('n3')==None:
                    a=1                                 #Para que no haga nada 
                          
                else:
                    FN.append(int(resultadoAuxi2.group('n3'))- 1)      
            
                auxi3 = resultado.group('tri3')
                resultadoAuxi3 = ERTripleta.fullmatch(auxi3)
                
                if resultadoAuxi3:
                    
                    if resultadoAuxi2.group('n3') == None:
                        a=1                                 #Para que no haga nada                
                    else:
                        FN.append(int(resultadoAuxi2.group('n3'))- 1)

    if valido == False:
        return False
    else:
        return True
        

if __name__ == '__main__':

    ficheroValido = r'(^[^0-9](\w|(-)?)*.obj)'
    ERFichero = re.compile(ficheroValido)

    flag = False

    print("Escriba el nombre del fichero: ")
    
    while flag == False:   
        
        fichero = input()
        
        if len(fichero) == 0:
                sys.exit()
        else:
            lista = listdir('.')
            
            for i in lista:
                
                if i == fichero:
                    resultado = ERFichero.fullmatch(fichero)
                    
                    if resultado : 
                        flag = True
                        print('El fichero es valido')
                        
            if flag == False :
                print('El fichero no es valido, pruebe con otro fichero:')
    
    
    
    numeroValido = r'(-?\d+(\.\d{1,7})?)([Ee](\+0+|-\d*[1-9]\d*|\+\d+))?'
    vValido = r'v +' + r'(?P<num1>' + numeroValido + ')' + r' +' + r'(?P<num2>' + numeroValido + ')' + r' +' + r'(?P<num3>' + numeroValido + ')' + r'( +' + numeroValido + ')?'
    ERV = re.compile(vValido)
    vnValidos = r'vn +' + r'(?P<num1>' + numeroValido + ')' + r' +' + r'(?P<num2>' + numeroValido + ')' + r' +' + r'(?P<num3>' + numeroValido + ')'
    ERVn = re.compile(vnValidos)
    vtValidos = r'vt +' + r'(?P<num1>' + numeroValido + ')' + r' +' + r'(?P<num2>' + numeroValido + ')' + r'( +' + r'(?P<num3>' + numeroValido + ')' + ')?'
    ERTexturas = re.compile(vtValidos)
    tripletaValida = r'((?P<n1>\d+)(/|/{2})?(?P<n2>\d+)?(/)?(?P<n3>\d+)?)'
    ERTripleta = re.compile(tripletaValida)
    fValidos = r'f +' + r'(?<tri1>' + tripletaValida + ')' + r' +' + r'(?<tri2>' + tripletaValida + ')' + r' +' + r'(?<tri3>' + tripletaValida + ')'
    ERF = re.compile(fValidos)
    
    V = []
    T = []
    N = []
    FV = []
    FT = []
    FN = []
    
    if leerFichero(fichero):
        print('El fichero introducido es valido')
        mostrar(V, T, N, FV, FT, FN) 
        
    else:
        print('El fichero introducido no es valido')
        