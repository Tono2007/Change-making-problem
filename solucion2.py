def makeChange2(monedas, cantidad):
    # Se crea una lista del tamaño de la cantidad + 1 con elementos con valor inicial nulo
    # Si la cantidad es 5 nos da--> [None, None, None, None, None, None] lista con 6 elementos nulos
    soluciones = [None] * (cantidad + 1)
    # Si la cantidad es 5 nos da--> [[], None, None, None, None, None]
    soluciones[0] = []
    # Empezando de la posición 0 encontraremos combinaciones para otras cantidades agregando los valores de las monedas
    for posicionActual in range(cantidad):
        # Si no tenemos una combinación para la posición actual no podemos sacar mas combinaciones a partir de esa
        if soluciones[posicionActual] != None:
            for moneda in monedas:
                # Cantidad de la nueva Combinacion a evaluar
                nuevaCombinacion = posicionActual + moneda
                if nuevaCombinacion <= cantidad:  # con esta condicion verificamos que la combinacion no de una suma por encima de la cantidad
                    # Si no existe una combinacion en la lista de soluciones para la cantidad de nueva combinación, se agrega o
                    # si la nuevaCombinacion es mejor que la actual se remplaza
                    if (soluciones[nuevaCombinacion] == None or
                        len(soluciones[nuevaCombinacion]) >
                            len(soluciones[posicionActual]) + 1):
                        soluciones[nuevaCombinacion] = soluciones[posicionActual] + [moneda]
    return soluciones[cantidad]
