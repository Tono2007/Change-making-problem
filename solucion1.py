from functools import lru_cache
# Solucion 1
# monedas debe ser una lista de enteros, cantidad debe ser un entero no menor que 0
def makeChange1(monedas, cantidad):
    if cantidad == 0:  # Validación cuando lleguemos a la cantidad 0
        return []
    if cantidad < 0:  # Validación para saber que llegamos a una cantidad negativa que no se puede pagar
        return None
    resultadoOptimo = None  # declaramos e inicializamos el resultadoOptimo que retornaremos
    for moneda in monedas:  # iteramos sobre cada moneda
        # llamamos a makeChange para obtener una posible solución
        # Restamos el valor actual de moneda para dividir en subproblemas
        # Aqui podemos obtener [], None o una posible combinación
        combinacion = makeChange1(monedas, cantidad - moneda)
        if combinacion != None:  # Validación para saber que es una posible combinacion
            # Validación para saber que es una posible combinacion
            candidata = combinacion + [moneda]
            # Comparamos si la solucion candidata es mejor que el resultadoOptimo actual lo remplazamos
            if (resultadoOptimo is None or len(candidata) < len(resultadoOptimo)):
                resultadoOptimo = candidata
    return resultadoOptimo

#Solución1 con cache
def makeChange11(monedas, cantidad):
    @lru_cache(maxsize=None)
    def helper(cantidad):
        if cantidad == 0:
            return []
        if cantidad < 0:
            return None
        resultadoOptimo = None
        for moneda in monedas:
            combinacion = helper(cantidad - moneda)
            if combinacion != None:
                candidata = combinacion + [moneda]
                if (resultadoOptimo is None or len(candidata) < len(resultadoOptimo)):
                    resultadoOptimo = candidata
        return resultadoOptimo
    return helper(cantidad)
