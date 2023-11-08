#Modificando parámetros mutables

def lista(arg, resultado=[]):
    resultado.append(arg)
    print(resultado)
lista('domingo', [])

#Ejercicio: Tomé el presente ejercicio, y pasé a la función la lista con los días de la semana restantes

#Definimos la función
def lista(dia, semana=[]):
    
    #Agregar a la lista Semana el dia insertado
    semana.append(dia)
    
    #Mostar la lsita Semana
    print(semana)

#Agregar Domingo al dia y a la lista los demas dias
    dia.append("Domingo")  #.APPEND agregar un valor nuevo
lista.apend(["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"])