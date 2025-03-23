import numpy as np
import matplotlib.pyplot as plt
import math
import random


#Set6


def get_names():
    return eval(input("Enter names list: "))

def q1():
    #use dict to store names and ages
    names_list = get_names()
    names_dict = {}
    for i in range(0, len(names_list), 2):
        names_dict[names_list[i]] = names_list[i + 1]
    print(names_dict)


def q2():
    names = get_names()
    output = []
    for i in range(0, len(names), 2):
        output.append((names[i], names[i + 1]))
    print(output)

def q3():
    #x + 2y + 3z = 2
    a1, b1, c1 = 1, 2, 3
    d1 = 2
    #4x + 8y + 66z = 3
    a2, b2, c2 = 4, 8, 66
    d2 = 3
    #7x + 81y + 9z = 4
    a3, b3, c3 = 7, 81, 9
    d3 = 4
    #Mx = b
    M = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
    b = np.array([d1, d2, d3])
    x = np.linalg.solve(M, b)
    print(x)


def q4():
    def d2b(x):
        result = ''
        if x == 0:
            result += '0'
        elif x == 1:
            result += '1'
        else:
            r = None
            q = None
            while q != 1:
                q = x//2
                r = x%2
                result += str(r)
                x = q
            result += '1'
        return int(result[::-1])
    numpy_DecimalToBinary = np.frompyfunc(d2b, 1, 1)
    A = np.random.randint(0, 100, 10)
    print('A:', A, '\n', 'Through pyfunc', numpy_DecimalToBinary(A), '\n', 'Actual: ', [int(bin(x)[2:]) for x in A])


def q5():
    arr1 = np.array([[50, 60, 70], [67, 88, 90], [60, 78, 97]])
    #1
    sum_marks = arr1.sum(axis = 1)
    print(f'Sum of marks\n{sum_marks}')
    #2
    sum_subjects = arr1.sum(axis = 0)
    print(f'Sum of subjects\n{sum_subjects}')

def q6():
    A = np.array([1, 2, 3, 4])
    B = np.array([3, 4, 5, 6])
    C = np.setdiff1d(A, B)
    print(C)

def q7():
    arr1 = np.array([[1, 2], [4, 5]])
    arr2 = np.array([[3, 3], [1,1]])
    print(np.multiply(arr1, arr2))
    print(np.matmul(arr1, arr2))


def q8():
    def f(x):
        return x*x*x + 1
    L = list(range(0, 11))
    Lout = [f(x) for x in L]
    A = np.array(L)
    Aout = f(A)
    print(Lout)
    print(Aout)

def q9():
    def f(x):
        output = None
        if x < 0: output = 0
        elif x == 0: output = 1
        else: output = x%3
        return output
    X = np.random.randint(-10, 10, 10)
    g = np.frompyfunc(f, 1, 1)
    print(g(X))
    h = np.vectorize(f, otypes = [int])
    print(h(X))

def q10():
    l_e, h_e = np.linspace(20, 21, 10, endpoint=True, retstep=True)
    l_we, h_we = np.linspace(20, 21, 10, endpoint=False, retstep=True)
    print(h_e)
    















