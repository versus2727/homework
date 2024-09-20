#вариант 8
import math

k= int(input("Задайте k:\n"))
x = -1


while True:
    f=x**5-2*k*x-11
    print("{0} {1:.2f} {2} {3:.4f}" .format("x =", x, "f(x) =", f))
    if 2*x>=3:
        f=(2-k*x+3*math.sin(x))**k
        print("{0} {1:.2f} {2} {3:.4f}" .format("x =", x, "f(x) =", f))
        break
    x+=13
    
    