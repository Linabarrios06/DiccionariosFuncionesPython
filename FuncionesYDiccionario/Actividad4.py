#Operaciones sobre los diccionarios
dicaleatorio={x: x**2 for x in (2, 4, 6)}
print(dicaleatorio)

#IMPRIMIR NÚMEROS EN REVERSA
print("Números en reversa")
for i in reversed(range(1, 10, 2)):
   print(i)

#BORRAR UN ELEMENTO DEL DICCIONARIO
del(calificaciones['Rosa']) #DEL La declaración se utiliza para eliminar objetos.
for i, j in calificaciones.items(): #.ITEMS: Cada par de clave-valor es denominado como elemento
   print(i,j) 