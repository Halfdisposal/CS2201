import numpy as np
import math 



def NewtonForward(X, y, value):
    n = len(X)
    u = (value - X[0])/(X[1] - X[0])
    table = np.zeros((n, n))
    table[:, 0] = y
    def u_calc(u, n):
        temp = u
        for i in range(1, n):
            temp *= (u  - i)
        return temp
    def fact(n):
        i = 1
        for j in range(1, n+1):
            i*=j
        return i
    for i in range(1, n):
        for j in range(n-i):
            table[j][i] = table[j+1][i-1] - table[j][i-1]
    print(f"Difference Table: \n{table}")
    interpolated_value = table[0][0]
    for i in range(1, n):
        interpolated_value += table[0][i]  * u_calc(u, i)/fact(i)
    return interpolated_value
    

def NewtonBackward(X, y, value):
    n = len(X)
    u = (value - X[-1])/(X[1] - X[0])
    table = np.zeros((n, n))
    table[:, 0] = y
    def u_calc(u, n):
        temp = u
        for i in range(1, n):
            temp *= (u  - i)
        return temp
    def fact(n):
        i = 1
        for j in range(1, n+1):
            i*=j
        return i
    for i in range(1, n):
        for j in range(i, n):
            table[j][i] = table[j][i-1] - table[j-1][i-1]
    print(f"Difference Table: \n{table}")
    interpolated_value = table[-1][0]
    for i in range(1, n):
        interpolated_value += table[-1][i]  * u_calc(u, i)/fact(i)
    return interpolated_value


def LagrangeInterpolation(X, y, value):
    result = 0
    n = len(X)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (value - X[j])/(X[i] - X[j])
        result += term 
    return result 




years = [2000, 2005, 2010, 2015, 2020]
production = [600, 650, 665, 600, 585]
v1 = 2004
print("Interpolated Value: ", NewtonForward(years, production, v1))
years = [45, 50, 55 ,60]
production = [0.7071, 0.766, 0.8192, 0.866]
v2  = 56
print("Interpolated Value: ", NewtonBackward(years, production, v2))
X = [ 5, 15, 30, 42, 55 ]
y = [250, 200, 150, 102, 75]
value = 50
print("Interpolated Value: ", LagrangeInterpolation(X, y, value))
