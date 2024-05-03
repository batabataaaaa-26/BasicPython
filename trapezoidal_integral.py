import math
from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

def trapezoidal(f, a, b, N):
    h = (b - a) / N
    S = 0
    for k in range(1, N+1):
        S += h/2 * (f(a+(k-1)*h) + f(a+k*h))
    return S

print(trapezoidal(sin, 0, math.pi/2, 100))
