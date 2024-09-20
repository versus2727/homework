#вариант 8

import math

k= int(input("Задайте k:\n"))
x = -1
while x <= 5:
    if 2*x<3:
        f=x**5-2*k*x-11
    else:
        f=(2-k*x+3*math.sin(x))**k
    x+=0.6
    print("{0} {1:.2f} {2} {3:.4f}" .format("x =", x, "f(x) =", f))