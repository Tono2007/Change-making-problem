def makeChange(monedas, cantidad):
    if cantidad == 0:
        print("amount === 0")
        return []
    if cantidad < 0:
        print("amount < 0")
        return None
    resultadoOptimo = None
    for moneda in monedas:
        combinacion = makeChange(monedas, cantidad - moneda)
        if combinacion != None:
            candidata = combinacion + [moneda]
            if (resultadoOptimo is None or
                    len(candidata) < len(resultadoOptimo)):
                resultadoOptimo = candidata
    return resultadoOptimo


makeChange([1, 2, 3], 5)
