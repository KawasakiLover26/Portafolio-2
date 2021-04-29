"""
Función: extremosLista
Entradas: una lista con contenido dentro
Salidas: El Numero mayor y menor de la lista
Restricciones: La lista no puede estar en blanco y su contenido deben ser numeros
"""

def extremosLista(lista):
        if(lista == []):
            return 0
        else:
            return extremosLista_aux((mayorLista(lista)),(menorLista(lista)))
        
def extremosLista_aux(lista, lista2):
    if(lista == lista2):
        lista3 = [lista]
        return lista3
    else:
        lista4 = [lista2,lista]
        return lista4
    


def mayorLista(lista):
    if lista == []:
        return "error"
    else:
        return mayorListaAux(lista[1:], lista[0])
    
def mayorListaAux(lista, resultado):
    if lista == []:
        return resultado
    elif lista[0] > resultado:
        return mayorListaAux(lista[1:], lista[0])
    else:
        return mayorListaAux(lista[1:], resultado)


def menorLista(lista):
    if lista == []:
        return "error"
    else:
        return menorListaAux(lista[1:], lista[0])
    
def menorListaAux(lista, resultado):
    if lista == []:
        return resultado
    elif lista[0] < resultado:
        return menorListaAux(lista[1:], lista[0])
    else:
        return menorListaAux(lista[1:], resultado)
                             










