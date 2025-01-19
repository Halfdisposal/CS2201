import numpy as np


def bijection(f, domain, lc):
    l, h = domain
    step = 1
    diff = inf
    iter = 1
    while diff > lc:
        print(f'while lopp no {iter}')
        iter +=1
        fl = f(l)
        fh = f(h)
        diff = fh-fl
        if fl*fh < 0 and diff<=lc:
            print(f"Found in {l}, {h}")
            break
        step = step/2
        fi = f(l+step)
        if fl*fi < 0:
            h = l+step
        if fi*fh < 0:
            l = l+step
    return diff



def f(x):
    return x**2 + 5*x + 3**x - 5
import time 
t1 = time.time()
bijection(f, (0, 10), 1e-7)
t2 = time.time()
print(t2-t1)
