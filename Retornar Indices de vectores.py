"""
Nombre: obtenerIndicesListaVectores
Entrada: Debe de ingresar tres vectores con contenido dentro
Salida: Devolver los indices de los vectores cuyo valor sean cero o un numero negativo
Restricciones: solo se pueden ingresar listas
"""

def obtenerIndicesListaVectores(vector1,vector2,vector3):
    if isinstance(v1,list) and isinstance(v2,list) and isinstance(v3,list):
        if LargoDelVector(v1) == LargoDelVector(v2) == LargoDelVector(v3):
            if(0==0):
                return validarDatosDelVector(v1,v2,v3)
            else:
                print("lol")
    else:
        print ("ERROR: Debe de ingresar solo listas")
            
           
def ValidacionDeIndice(vector,indice,NuevaLista):
    if vector== []:
        return NuevaLista
    elif vector[0]<=0:
        return ValidacionDeIndice(vector[1:],indice+1,NuevaLista+[indice])
    else:
        return ValidacionDeIndice(vector[1:],indice+1,NuevaLista)

def LargoDelVector(v1):
    if v1==[]:
        return 0
    else:
        return LargoDelVector_aux(v1,0)

def LargoDelVector_aux(vector,resultado):
    if vector==[]:
        return resultado
    else:
        return LargoDelVector_aux(vector[1:],resultado+1)

def validarDatosDelVector(vector1,vector2,vector3):
    if vector1==[] and vector2==[] and vector3==[]:
        print("ERROR: No puede ingresar una lista en blanco")
    else:
        if isinstance(vector1[0],int) and isinstance(vector2[0],int) and isinstance(vector3[0],int):
            return listaVectores(vector1[1:],vector2[1:],vector3[1:], vector1, vector2, vector3)
        else:
            return print("lol")

def listaVectores(v1,v2,v3, vector1, vector2, vector3):
    if (0==0):
        vector4 = ValidacionDeIndice(vector1,0,[])
        vector5 = ValidacionDeIndice(vector2,0,[])
        vector6 = ValidacionDeIndice(vector3,0,[])
        vector7 = [vector4]+[vector5]+[vector6]
        return vector7
