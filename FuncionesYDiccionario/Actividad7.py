#Funciones con Parámetros
def raiz(value):
    return value ** (1/2)
print(f'La raiz cuadrada es: {raiz(4)}')

def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")

validarsiexiste(1)


#Ejercicio
#Escriba una función en Python que reproduzca lo siguiente:
#𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2 Valor para X=3 y valor para Y=5#
# Definimos la función
def Tarea(x,y): 

    #Operacion que nos pide el ejercicio 
    resultado= x*2 + y*2
    
    #Mostramos el resultado
    print(f"\nEl resultado de la operación de \n {x} x 2 + {y} x 2 es: {resultado}")

#Pedimos los valores 
Tarea(int(input("Digite el valor de X: ")), int(input("Digite el valor de Y: ")))