import numpy as np
import matplotlib.pyplot as plt


def Rectangular(f, domain, n):
    a, b = domain
    x, h = np.linspace(a, b, n + 1, retstep = True)
    y = f(x[:-1])
    area = np.sum(y * h)
    return area

def Trapezoidal(f, domain, n):
    a, b = domain
    x, h = np.linspace(a, b, n + 1, retstep = True)
    y = f(x)
    area = h *(((y[0] + y[-1])/2) + np.sum(y[1: -1]))
    return area 

def Simmpson(f, domain, n):
    a, b = domain
    x, h = np.linspace(a, b, n + 1, retstep = True)
    y = f(x)
    area = (h/3) * (y[0] + y[-1] + 4 * np.sum(y[1: -1: 2]) + 2*np.sum(y[2: -1: 2]))
    return area

