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

arr = create_random_list(100)
start = timeit.default_timer()
quicksort_inplace(arr, 0, len(arr)-1)
stop = timeit.default_timer()
print(arr)
print("RUNTIME: " + str(stop-start) )

start = timeit.default_timer()
my_quicksort(arr)
stop = timeit.default_timer()
print(arr)
print("RUNTIME: " + str(stop-start) )


