
#вариант 8



import math

x = int(input("Задайте x:\n"))
k = int(input("Задайте k:\n"))
if 2*x<3:
    f=x**5-2*k*x-11
    print("Поскольку x =", x, ", а k =", k, ", то подходит условие: ", 2, "*", x, "< 3")
    print("f =", f)
else:
    f=(2-k*x+3*math.sin(x))**k
    print("Поскольку x =", x, ", а k =", k, ", то подходит условие: ", 2, "*", x, ">= 3")
    print("f=",f)
