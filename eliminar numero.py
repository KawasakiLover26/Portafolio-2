"""
Función: eliminarDigito
Entradas: un numero que sera el princiapl y otro numero que servira para sea eliminado en el primer numero ingresado
Salidas: El numero sin el segundo numero ingresado
Restricciones: La lista no puede estar en blanco
"""
def eliminarDigito(num, NumeroAEliminar):
    if(num == 0):
        return print("Error: el numero no puede ser cero")
    else:
        return EliminaDigito_aux(num, NumeroAEliminar, 0, num%10,1)

def EliminaDigito_aux(num, NumeroAEliminar, resultado, num2, variable):
    if(num>0):
        resultado = resultado+num2*variable
        return EliminaDigito_aux(num//10, NumeroAEliminar,resultado , num2%10,variable * 10)
    elif(num==0):
        return resultado
    print(resultado)
        
