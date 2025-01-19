import matplotlib.pyplot as plt
import numpy as np
from math import log10
from typing import Callable
from functools import lru_cache
from math import sin

@lru_cache(maxsize = 128)
def tabular(func: Callable[[float], None], domain: tuple, accuracy: float) -> None:

    '''Calculates almost for any root except if tangent
    @params
    function: function
    domain: tuple, eg: (0, 1)
    accuracy: float, eg: 0.1'''
    low, high = domain
    f = func
    a = accuracy
    step = high - low 
    f_l = f(low)

    iter = 0
    while step > a:
        step = (high-low)/10
        iter += 1
        print('while loop no |',iter)        
        dev = 1
        #round_int = int(log10( round(1/step)))
        round_int = iter
        for i in np.arange(low, high+step, step):
            f_l = f(i)
            f_h = f(i+step)
            print(f' for loop no  |{iter}.{dev}')
            dev += 1
            if f_l*f_h <= 0:
                low = i.item()
                high = i.item()+step 
                root = round(low, round_int) + round(high, round_int)
                root /= 2
                print(f'Range = ({round(low, round_int)}, {round(high, round_int)})'+f' likely root = {root}')
                break

        

def f(x):
    return sin(x) + x*x - 1

import time 
t1 = time.time()
tabular(f, (0, 1), 1e-5)
t2 = time.time()
print('Time taken = ', t2-t1)