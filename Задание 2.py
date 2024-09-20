#вариант 2
import math
import numpy

k1 = 1
k2 = 0

for b in numpy.arange(-3,3.1,0.5):
    if (b+1) == 0: continue
    if math.cos((b)**2)-k2 <= 0 : continue
    y=(k1/(b+1)) + math.log10(math.cos(b**2)-k2)
    print("b =", "%.2f" % b, " y(b) =", "%.4f" % y)