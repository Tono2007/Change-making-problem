import solucion1
import time

monedas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

begin = time.time()
print(solucion1.makeChange2(monedas, 20))
end = time.time()
print("Tiempo: ", end-begin)


begin = time.time()
print(solucion1.makeChange(monedas, 20))
end = time.time()
print("Tiempo: ", end-begin)
