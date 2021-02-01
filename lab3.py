import random
import math

import timeit
import pandas as pd
from sort import *

def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

###### TESTING ######
def avg(L):
    return sum(L) / len(L)

def tests(trials):
    std, dual, tri, quad, inplace = [], [], [], [], []
    
    for i in range(trials):
        x = create_random_list(100)

        arr = x.copy()
        start = timeit.default_timer()
        my_quicksort(arr)
        stop = timeit.default_timer()
        std.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        dual_pivot_quicksort(arr)
        stop = timeit.default_timer()
        dual.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        tri_pivot_quicksort(arr)
        stop = timeit.default_timer()
        tri.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        quad_pivot_quicksort(arr)
        stop = timeit.default_timer()
        quad.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        quicksort_inplace(arr, 0, len(arr)-1)
        stop = timeit.default_timer()
        inplace.append(stop - start)

    #averages = {"std": avg(std), "dual": avg(dual), "tri": avg(tri), "quad": avg(quad), "inplace": avg(inplace)}
    print("AVERAGES: std, dual, tri, quad, inplace")
    print(avg(std), avg(dual), avg(tri), avg(quad), avg(inplace))

    print("MINIMUM: std, dual, tri, quad, inplace")
    print(min(std), min(dual), min(tri), min(quad), min(inplace))

    print("MAXIMUM: std, dual, tri, quad, inplace")
    print(max(std), max(dual), max(tri), max(quad), max(inplace))
