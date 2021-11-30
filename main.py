#Solucion 1
#monedas debe ser un arreglo de enteros, cantidad debe ser un entero no menor que 0
def makeChange(monedas, cantidad): 
    if cantidad == 0: #Validación cuando lleguemos a la cantidad 0
        return []
    if cantidad < 0: #Validación para saber que llegamos a una cantidad negativa que no se puede pagar
        return None
    resultadoOptimo = None #declaramos e inicializamos el resultadoOptimo que retornaremos
    for moneda in monedas: #iteramos sobre cada moneda
        #llamamos a makeChange para obtener una posible solución
        #Restamos el valor actual de moneda para dividir en subproblemas
        combinacion = makeChange(monedas, cantidad - moneda) #Aqui podemos obtener [], None o una posible combinación
        if combinacion != None: #Validación para saber que es una posible combinacion
            candidata = combinacion + [moneda] #Validación para saber que es una posible combinacion
            #Comparamos si la solucion candidata es mejor que el resultadoOptimo actual lo remplazamos
            if (resultadoOptimo is None or len(candidata) < len(resultadoOptimo)):
                resultadoOptimo = candidata
    return resultadoOptimo


makeChange([1, 2, 3], 5)
