#Modificando parámetros mutables

def listalimpia(arg, result=None): #denota falta de valor. Este objeto no tiene métodos

    if result is None:
        result = [] #[]Lista vacia 
        result.append(arg) #.APPEND es para agregar un nuevo valor 
    print(result)

listalimpia("a") 

listalimpia("b") 