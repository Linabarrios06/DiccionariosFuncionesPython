#Parámetros por defecto

def compra(marca,cantidad,valor=2500000): #DEF indica que una nueva función está siendo definida

    return dict( #RETURN significa retornar o devolver
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad #se multiplica valor por cantidad
    )

print(f' lo comprado fue:{compra("AMD",3)}')