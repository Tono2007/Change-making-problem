# Change-making-problem / Cambio de monedas

## Entendiendo el problema
Dada una cantidad de dinero y una lista de denominaciones de monedas, encontrar el número mínimo de monedas (de determinadas denominaciones) que suman la cantidad de dinero exacta.

*Es un subcaso especial del problema de la mochila*
### Ejemplo1:
Pagar la cantidad de 10 usando las siguientes monedas [2,3,5,6]
Tenemos 7 posibles combinaciones de cambios {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5}, {5,5}

Donde la mejor combinación es {5,5} que usa la menor cantidad de monedas

## Consideraciones
- Este problema supone que todas las monedas están disponibles infinitamente.
- Dado el caso donde la cantidad de dinero es 0 el resultado sera una lista vacia []
- Dado el caso donde no es posible pagar la cantidad con las monedas proporcionadas retornar nulo. Ejemplo cantidad=5 monedas[2,4]

## Solucion 1
La primera solucion contempla todas las posibles combinaciones, podemos implementarla dividiendo en pequeños subproblemas y aplicando recursividad.

Por cada moneda hacemos una resta de la cantidad de dinero menos el valor de la moneda de esta forma obtenemos un punto de inicio de cada combinación y dividimos el problema en subproblemas. Aqui podemos aplicar recursividad y continuar haciendo las restas mientras la cantidad a pagar disminuye y llega a 0, de esta forma obtenemos todas las posibles combinaciones. En esta parte necesitamos hacer una validación para detener la iteración cuando la cantidad llegue a igual o menor que 0 (Si llega a 0 sabemos que es una posible solución).

Seguido de esto necesitamos encontrar la mejor solucion que use la menor cantidad de monedas, necesitamos hacer una comparacion para obtener la mejor solución de cada suproblema, guardarla y retornar la combinacion con menor cantidad de monedas por cada nivel (cada vez que disminuimos la cantidad a pagar).
*Por eso esta primera solución es una estrategia de análisis top-down (de arriba hacia abajo)*

Ejemplo de divición de subproblemas para el caso, monedas: [1,2,3] y cantidad de 5 
![subPrograms](./images/subPrograms.png)

```py
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
```

![subPrograms](./images/Ejemplo-1.png)

Notemos que tenemos subproblemas que se repiten, dada la recursividad y el uso de todas las combinaciones posibles esta solucion tiene una complejidad exponencial y poco rendimiento.