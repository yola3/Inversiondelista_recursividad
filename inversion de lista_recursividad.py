# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:34:13 2020

@author: HACKER
"""

listas=[1,2,3,4,5,6,7,8,9,10]# aqui ya tengo los dijitos que voya ocupar
def invertir_lista (listas): # la funcion 
    if listas ==[]:# aqui pongo la condicion que si llegamos al caso base nos devuelva un resulatdo
        return listas ## aqui retorno la lista
    else:# si no se da ese caso tenemos que coger el ultimo elemento y concatenarlo al resto
        return[listas[-1]]+invertir_lista(listas[:-1])#retornamos al ultimo elemento de lista pero que tiene que estar en una lista  # se llama asi mismo la funcion creando un bucle y 
        #terminara cuando se cumpla la condision o el caso base
  
     
        
print("los numeros inversos") #mandamos un mensaje y lo ejecutamos
print(invertir_lista(listas))# mandamos a imprimir la lista

        