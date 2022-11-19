from math import sqrt
import numpy as np
import math

expr =[(1/(4*math.sqrt(2*math.pi)))*math.exp((-1*(x+2)**2)/32) for x in np.arange(-100,100,0.1)]
print(np.var(expr))
print(np.std(expr))
print(np.average(expr))
