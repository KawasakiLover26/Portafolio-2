"""
Función: NivelesLista
Entradas: una lista con contenido dentro
Salidas: La lista invertida
Restricciones: La lista no puede estar en blanco
"""
def nivelesLista(lista):
    if isinstance(lista,list):
        return nivelesLista_aux(lista,[])
    else:
        print("ERROR: Debe de ingresar una lista")

def nivelesLista_aux(lista,listanueva):
    if lista==[]:
        return listanueva
    elif( lista!= []):
       Divisor=dividirlista(lista[0],1)
       return nivelesLista_aux(lista[1:],listanueva+[Divisor])
    else:
        return nivelesLista_aux(lista[1:],listanueva+[0])

def dividirlista(lista,listanueva):
    if lista==[]:
        return listanueva
    else:
        if isinstance(lista,list):
            return dividirlista(lista[0],listanueva+1)
        else:
            return 1
