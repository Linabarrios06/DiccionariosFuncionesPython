#Funciones anónimas «lambda»
#Una función lambda tiene las siguientes propiedades:

#1. Se escribe con una única sentencia.
#2. No tiene nombre (anónima).
#3. Su cuerpo tiene implícito un return.
#4. Puede recibir cualquier número de parámetros.

#Ejemplo:

numero_palabras = lambda t: len(t.strip().split()) #LAMBADA: es el método del código de la función que procesa eventos.
#La función se ejecuta hasta que el controlador devuelve una respuesta, se cierra o se agota el tiempo de espera.
#.STRIP:suprime blancos u otro carácter especificado del final o del principio de una expresión de serie
#.SPLIT:dividir cadenas en lugares concretos
print(numero_palabras("hola, esto es una prueba con lambda"))