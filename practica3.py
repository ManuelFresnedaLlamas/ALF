#-*- coding: UTF-8 -*-
'''
Created on 26 jun. 2020

@autores: David Martinez Pozuelo, Manuel Fresneda Llamas
'''
import regex as re
import sys






def getFichero():
    global nombreFichero
    patronTXT=r'(.*?)(\.txt)'
    erTXT=re.compile(patronTXT)
    
    print('Introduce el nombre del fichero con formato .txt:')
    nombreFichero=input()
    
    if len(nombreFichero)==0:
        print('No has introducido ningún fichero')
        
    if erTXT.fullmatch(nombreFichero):
        try:
            archivo=open(nombreFichero, "r", encoding="utf8")
            return archivo
        except FileNotFoundError:
            print('No se encontró el archivo introducido.', file = sys.stderr)
    else:
        print('El fichero introducido no es valido', file = sys.stderr)
        
    
def leerYCrearFichero(archivo):    
    
    print('¿Cuál quieres que sea la longitud de la línea?:')
    longitudLinea=int(input())
    while longitudLinea<10:
        print("El número debe ser mayor o igual a 10")
        longitudLinea=int(input())
    
    auxFicheroNuevo = nombreFichero.split(".txt")
    nombreFicheroNuevo=auxFicheroNuevo[0]+"_g.txt" #así tenemos el nombre correcto _g.txt
    
    ficheroNuevo=open(nombreFicheroNuevo, "w", encoding="utf8")
    
    
    #################CUIDAO#####################
    #en nuestras lineas cualquier palabra seguirá el siguiente patron
    patronPalabra = r'(([^ \t\n]+)([ \t\n]))'
    erPalabra=re.compile(patronPalabra)
    
    palabraActual=""
    final=""
    for linea in archivo:
        for i in linea:
            palabraActual=palabraActual+i #Acumulamos las letras 1a1 hasta formar una palabra
            palabraValida=erPalabra.fullmatch(palabraActual)
            
            if palabraValida:
                if len(final) + len(palabraValida.group(2)) <= longitudLinea:
                    final=final+palabraValida.group(2)
                    palabraActual=''
                    if len(final) < longitudLinea:
                        final=final+palabraValida.group(3)
                        if palabraValida=='\n':
                            ficheroNuevo.write(final)
                            final=''
                    elif len(final) == longitudLinea:
                        final=final+'\n'
                        ficheroNuevo.write(final)
                        final=''
                else:
                    palabraDividia = reglasPalabras(palabraValida.group(2)) #funcion encargado de todas las divisiones d epalabras
                    if palabraDividia==[]:
                        final=final+'\n'
                        ficheroNuevo.write(final)
                        final=""
                    else:
                        flag=False
                        iterador=len(palabraDividia)-1
                        aux=""
                        while iterador!=-1:
                            aux=""
                            itPalDividida=palabraDividia[iterador]
                            for i in itPalDividida:
                                aux=aux+i
                                if i=='-':
                                    break
                            if len(final)+len(aux)<=longitudLinea:
                                if len(aux)==1 and len(final)+len(aux)<=longitudLinea: #Condicion extremadamente ESPECIAL xD para "Capítulo 1:"
                                    break
                                else:
                                    final=final+aux+'\n'
                                    ficheroNuevo.write(final)
                                    flag=True
                                if palabraValida.group(3)=='\n':
                                    final=palabraActual[(len(aux)-1):len(palabraActual)]
                                    ficheroNuevo.write(final)
                                    final=""
                                else:
                                    final=palabraActual[(len(aux)-1):len(palabraActual)]
                                break
                            iterador=iterador-1
                        if flag==False:
                            if palabraValida.group(2)=='\n': #FALLA CON QUIJO-////TE DE LA MANCHA
                                final=final+palabraActual+'\n'
                                ficheroNuevo.write(final)
                                final=""
                            else:
                                final=final+'\n'
                                ficheroNuevo.write(final)
                                final=palabraActual
                                
                    palabraActual=""
                
            elif palabraActual == ' ' or palabraActual =='\n':
                palabraActual=""
        if final != "":
            final=final
            ficheroNuevo.write(final)
            final=""
            
    
def reglasPalabras(palabra):
    
    regla1=r'([aeiouáéíóúüAEIOUÁÉÍÓÚÜ])([bcdfghjkmnñpqstvwxyzBCDFGHJKMNÑPQSTVWXYZ]|l{1,2}|L{1,2}|r{1,2}|R{1,2}|ch|CH)([aeiouáéíóúüAEIOUÁÉÍÓÚÜ]|y([ ;.,:?!\n\t]))'
    ERregla1 = re.compile(regla1)
    
    regla2a=r'([aeiouáéíóúüAEIOUÁÉÍÓÚÜ])(([pcbgfPCBGF])([rlRL])|([dtDT])(rR))([aeiouáéíóúüAEIOUÁÉÍÓÚÜ]|y([ ;:.,\n\t?!]))'
    ERregla2a = re.compile(regla2a)

    regla2b = r'([aeiouáéíóúüAEIOUÁÉÍÓÚÜ])(([dhjklmnñqrstvwxyzDHJKLMNÑQRSTVWXYZ]|l{1,2}|L{1,2}|r{1,2}|R{1,2}|ch|CH)|([bcfghjklmnñpqrsvwxyzBCDFGHJKLMNÑPQSTVWXYZ]|l{1,2}|L{1,2}|r{1,2}|R{1,2}|ch|CH)([bcdfghjklmnñpqstvwxyzBCDFGHJKLMNÑPQSTVWXYZ]|l{1,2}|L{1,2}|r{1,2}|R{1,2}|ch|CH))([aeiouáéíóúüAEIOUÁÉÍÓÚÜ]|y([ ;.,\n\t:?!]))'
    ERregla2b = re.compile(regla2b)
   
    regla3a = r'([aeiouáéíóúüAEIOUÁÉÍÓÚÜ])([bcdfghjkmnñpqstvwxyzBCDFGHJKMNÑPQSTVWXYZ]|l{1,2}|L{1,2}|r{1,2}|R{1,2}|ch|CH)(([pcbgf])([rl])|([dt])(r))([aeiouáéíóúüAEIOUÁÉÍÓÚÜ]|y([ ;.,\n\t:?!]))'
    ERregla3a = re.compile(regla3a)
    
    regla3b = r'([aeiouáéíóúüAEIOUÁÉÍÓÚÜ])(([bdnmlrBDNMLR][sS])|([sS][tT]))([bcdfghjkmnñpqstvwxyzBCDFGHJKMNÑPQSTVWXYZ]|l{1,2}|L{1,2}|r{1,2}|R{1,2}|ch|CH)([aeiouáéíóúüAEIOUÁÉÍÓÚÜ]|y([ ;.,\n\t:?!]))'
    ERregla3b = re.compile(regla3b)
   
    regla4 = r'([aeiouáéíóúüAEIOUÁÉÍÓÚÜ])(([bdnmlrBDNMLR][sS])|([sS]|[tT]))(([pcbgfPCBGF])([rlRL])|([dtDT])(rR))([aeiouáéíóúüAEIOUÁÉÍÓÚÜ]|y([ ;.,\n\t:?!]))'
    ERregla4 = re.compile(regla4)
    
    auxPalabra = palabra
    palabraDividida=[]
    palabraActual=""
    dobleConsonantes={"ch","ll","rr"}
    for i in range(0,len(palabra)):
        match1=ERregla1.match(auxPalabra)
        match2a=ERregla2a.match(auxPalabra)
        match2b=ERregla2b.match(auxPalabra)
        match3a=ERregla3a.match(auxPalabra)
        match3b=ERregla3b.match(auxPalabra)
        match4=ERregla4.match(auxPalabra)
    
        #Ahora hacemos las comprobaciones
        if match1: #ejemplo : u-no -> grupo(1) + '-' + resto(desde 1 hasta tamaño)
            palabraDividida.append(palabraActual+match1.group(1)+'-'+auxPalabra[1:len(auxPalabra)])
        elif match2a: #i-glu mismo razonamiento
            palabraDividida.append(palabraActual+match2a.group(1)+'-'+auxPalabra[1:len(auxPalabra)])  
        elif match2b:
            if len(match2b.group(1))==1:
                if match2b.group(2)[0:2] in dobleConsonantes:  
                    palabraDividida.append(palabraActual+match2b.group(1)+match2b.group(2)[0:2]+'-'+match2b.group(2)[2]+auxPalabra[4:len(auxPalabra)])
                else:
                    palabraDividida.append(palabraActual+match2b.group(1)+match2b.group(2)[0]+'-'+match2b.group(2)[1:3]+auxPalabra[4:len(auxPalabra)])
        elif match3a:
            palabraDividida.append(palabraActual+auxPalabra[0:2]+'-'+auxPalabra[2:len(auxPalabra)])
        elif match3b:
            palabraDividida.append(palabraActual+auxPalabra[0:3]+'-'+auxPalabra[3:len(auxPalabra)])
        elif match4:
            palabraDividida.append(palabraActual+auxPalabra[0:3]+'-'+auxPalabra[3:len(auxPalabra)])
        
        palabraActual=palabraActual+auxPalabra[0]
        auxPalabra=auxPalabra[1:len(auxPalabra)]
    if palabraDividida!=[]:
        return palabraDividida
    else:
        return palabra  
if __name__ == '__main__':
    archivo=getFichero()
    if archivo!=None:
        leerYCrearFichero(archivo)