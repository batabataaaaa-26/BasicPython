import math
from math import sin

def trapezoidal(f, a=0, b=1, n=100):
    h = (b - a) / n
    S = 0
    for k in range(1, n+1):
        S += h/2 * (f(a+(k-1)*h) + f(a+k*h))
    return float(S)

print("(1):", trapezoidal(math.sin, 0, math.pi/2, 50))

print("(2):", trapezoidal(lambda x: 4 / (1 + x**2), 0, 1, 100))

print("(3):", trapezoidal(lambda x: math.sqrt(math.pi) * math.exp(-x**2), -100, 100, 1000))
