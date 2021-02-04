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

    averages = {"std": avg(std), "dual": avg(dual), "tri": avg(tri), "quad": avg(quad), "inplace": avg(inplace)}
    print("AVERAGES: std, dual, tri, quad, inplace")
    print(avg(std), avg(dual), avg(tri), avg(quad), avg(inplace))

    print("MINIMUM: std, dual, tri, quad, inplace")
    print(min(std), min(dual), min(tri), min(quad), min(inplace))

    print("MAXIMUM: std, dual, tri, quad, inplace")
    print(max(std), max(dual), max(tri), max(quad), max(inplace))

# Yi Luo begin
def create_sorted_list(n):
    res = []
    for i in range(n):
        res.append(i)
    return res

def average_vs_worst_case_performance():
    std_average, std_worst = [], []
    n = []
    for i in range(500):
        n.append(i)
        x = create_random_list(i)
        y = create_sorted_list(i)

        start = timeit.default_timer()
        my_quicksort(x)
        stop = timeit.default_timer()
        std_average.append(stop - start)

        start = timeit.default_timer()
        my_quicksort(y)
        stop = timeit.default_timer()
        std_worst.append(stop - start)

    df = pd.DataFrame({"n": n, "std_average": std_average, "std_worst": std_worst})
    df.to_csv("average_vs_worst_case_performance.csv", index=False)

def bubblesort(arr): 
    n = len(arr) 
    for i in range(n-1):  
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubblesort_vs_quicksort_vs_factor():
    bubblesort_runtime, quicksort_runtime = [], []
    factor = []
    for i in range(100):
        factor.append(i/100)
        x = create_near_sorted_list(996, i/100)

        arr = x.copy()
        start = timeit.default_timer()
        my_quicksort(arr)
        stop = timeit.default_timer()
        quicksort_runtime.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        y = bubblesort(arr)
        stop = timeit.default_timer()
        bubblesort_runtime.append(stop - start)

    df = pd.DataFrame({"factor": factor, "bubblesort_runtime": bubblesort_runtime, "quicksort_runtime": quicksort_runtime})
    df.to_csv("bubblesort_vs_quicksort_vs_factor.csv", index=False)

def selectionSort(l):
    for fillslot in range(len(l)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if l[location]>l[positionOfMax]:
                positionOfMax = location
        temp = l[fillslot]
        l[fillslot] = l[positionOfMax]
        l[positionOfMax] = temp

def selectionSort_vs_quicksort_vs_factor():
    selectionSort_runtime, quicksort_runtime = [], []
    factor = []
    for i in range(100):
        factor.append(i/100)
        x = create_near_sorted_list(996, i/100)

        arr = x.copy()
        start = timeit.default_timer()
        my_quicksort(arr)
        stop = timeit.default_timer()
        quicksort_runtime.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        y = selectionSort(arr)
        stop = timeit.default_timer()
        selectionSort_runtime.append(stop - start)

    df = pd.DataFrame({"factor": factor, "selectionSort_runtime": selectionSort_runtime, "quicksort_runtime": quicksort_runtime})
    df.to_csv("selectionSort_vs_quicksort_vs_factor.csv", index=False)

def insertionSort(l):
    for index in range(1,len(l)):
        currentvalue = l[index]
        position = index
        while position>0 and l[position-1]>currentvalue:
            l[position]=l[position-1]
            position = position-1
        l[position]=currentvalue

def insertionSort_vs_quicksort_vs_factor():
    insertionSort_runtime, quicksort_runtime = [], []
    factor = []
    for i in range(100):
        factor.append(i/100)
        x = create_near_sorted_list(996, i/100)

        arr = x.copy()
        start = timeit.default_timer()
        my_quicksort(arr)
        stop = timeit.default_timer()
        quicksort_runtime.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        y = insertionSort(arr)
        stop = timeit.default_timer()
        insertionSort_runtime.append(stop - start)

    df = pd.DataFrame({"factor": factor, "insertionSort_runtime": insertionSort_runtime, "quicksort_runtime": quicksort_runtime})
    df.to_csv("insertionSort_vs_quicksort_vs_factor.csv", index=False)

#average_vs_worst_case_performance()
#bubblesort_vs_quicksort_vs_factor()
#selectionSort_vs_quicksort_vs_factor()
#insertionSort_vs_quicksort_vs_factor()
# Yi Luo end

# Tests for small lists to talk about in report
def small_lists_tests(trials):
    std, insertion, selection, final  = [], [], [], []
    
    for i in range(trials):
        x = create_random_list(10)

        arr = x.copy()
        start = timeit.default_timer()
        insertion_sort(arr, 0, len(arr) - 1)
        stop = timeit.default_timer()
        insertion.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        my_quicksort(arr)
        stop = timeit.default_timer()
        std.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        selection_sort(arr)
        stop = timeit.default_timer()
        selection.append(stop - start)

        arr = x.copy()
        start = timeit.default_timer()
        final_sort(arr, 0, len(arr) - 1)
        stop = timeit.default_timer()
        final.append(stop - start)

    averages = {"std": avg(std), "insertion": avg(insertion), "selection": avg(selection), "final": avg(final)}
    print("AVERAGES:")
    print(averages)

tests(10000)
small_lists_tests(100)
