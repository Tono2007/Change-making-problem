import solucion1
import solucion2
import time

monedas = [1, 2, 3]
cantidad = 5
print(f"Monedas: {monedas}")
print(f"Cantidad: {cantidad}\n\n\n")

begin = time.time()
print(f"Solucion 1 resultado: {solucion1.makeChange1(monedas, cantidad)}")
end = time.time()
print(f"Tiempo Solucion1: {end-begin}\n")


begin = time.time()
print(
    f"Solucion 1 con cache resultado: {solucion1.makeChange11(monedas, cantidad)}")
end = time.time()
print(f"Tiempo Solucion1 con cache: {end-begin}\n")


begin = time.time()
print(f"Solucion 2 resultado: {solucion2.makeChange2(monedas, cantidad)}")
end = time.time()
print(f"Tiempo Solucion2: {end-begin}\n")
