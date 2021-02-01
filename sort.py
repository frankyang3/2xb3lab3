import math
import random

def quicksort_inplace(L,low, hi):
    if(low < hi):
        p = partition_inplace(L, low, hi)
        quicksort_inplace(L, low, p - 1)
        quicksort_inplace(L, p + 1, hi)

def partition_inplace(L, low, hi):
        ## pivot is L[hi]
        pivot = L[hi]
        small = low-1
        for i in range(low, hi):
                if L[i] < pivot:
                        small = small + 1
                        L[small], L[i] = L[i], L[small]
        L[small+1], L[hi] = L[hi], L[small+1]
        return (small+1)


