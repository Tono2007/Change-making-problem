import solucion1
import time

monedas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad=20

begin = time.time()
print(solucion1.makeChange(monedas, cantidad))
end = time.time()
print("Tiempo Solucion1: ", end-begin)


begin = time.time()
print(solucion1.makeChange2(monedas, cantidad))
end = time.time()
print("Tiempo Solucion1 con cache: ", end-begin)
