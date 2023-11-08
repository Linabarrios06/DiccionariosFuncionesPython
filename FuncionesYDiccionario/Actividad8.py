#Funciones con Parámetros Posicionales

def compra(marca,cantidad,valor): #DEF indica que una nueva función está siendo definida

    return dict(marca=marca,cantidad=cantidad,valor=valor*cantidad) #RETURN significa retornar o devolver
           #DICT (diccionario) es un tipo de dato que relaciona términos y significados
print(f' lo comprado fue:{compra("AMD",3,2500000)}')

#Funciones con Parámetros Nominales

def compra(marca,cantidad,valor):

    return dict(marca=marca,cantidad=cantidad,valor=valor*cantidad)
print(f'lo comprado fue:{compra(marca="AMD",cantidad=3,valor=2500000)}')