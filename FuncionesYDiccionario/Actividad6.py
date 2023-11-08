#Funciones con Parámetros

def raiz(value): 
    return value ** (1/2)
print(f'La raiz cuadrada es: {raiz(4)}')

def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")#Es verdadero

    else:
        print(f"{obj} is False")#Es falso

validarsiexiste(1)