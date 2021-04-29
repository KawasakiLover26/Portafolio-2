"""
Función: invertirLista
Entradas: una lista con contenido dentro
Salidas: La lista invertida
Restricciones: La lista no puede estar en blanco
"""
def invertirLista(lista):
    if(lista == []):
        return 0
    elif(lista != []):
        return invertirLista_aux(lista, [])


def invertirLista_aux(lista, lista2):
    if(lista == []):
        return lista2
    else:
        lista2=lista2+[lista[-1]]
        return invertirLista_aux(lista[:-1],lista2)

   
        
