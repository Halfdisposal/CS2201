import numpy as np
import matplotlib.pyplot as plt
import math
import random

def Tabular(h, f, domain):
    a, b = domain
    root = None 
    while f(a) * f(a + h) > 0 and a + h <= b:
        root = (a+h, a+2*h)
        a = a+h
    print(f'Root at: {root}') 
    return root

def Bijection(h, f, domain):
    a, b = domain 
    root = None 
    found = False 
    while not found:
        mid = (a + b)/2
        if f(a) * f(mid) < 0:
            b = mid
        elif f(mid) * f(b) < 0:
            a = mid 
        else:
            print('Root Not Found')
            break
        found = abs(f(a) - f(b)) <= h 
    root = (a, b)
    print(f'Root at {root}')

def NewtonRapson(h, f, domain):
    def df(f, x):
        dh = 1e-7
        return (f(x + dh) - f(x))/dh
    a, b = domain 
    found = False 
    start = b
    while not found:
        start -= (f(start)/df(f, start))
        found = abs(f(start)) <= h 
        print(f'Root at {start}')


def RegulaFalsi(h, f, domain):
    a, b = domain 
    found = False 
    x0 = a 
    x1 = b 
    iter = 0
    while not found:
        iter += 1
        mid = x0 - ((x1 - x0) * f(x0) / (f(x1) - f(x0)))
        if f(x0) * f(mid) <= 0:
            x1 = mid 
        elif f(mid) * f(x1) <= 0:
            x0 = mid 
        found = abs(f(mid)) <= h 
    print(f'Root found at {mid} after {iter} iterations')



def f(x):
    return 10**x + x - 4



if __name__ =="__main__":
    RegulaFalsi(0.01, f, (0.5, 0.6))
