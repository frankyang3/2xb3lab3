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

def dual_pivot_quicksort(L):
    copy = dual_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def dual_pivot_quicksort_copy(L):
        if len(L) < 2:
                return L
        if L[0] <= L[1]:
                pivot1,pivot2 = L[0], L[1]
        else:
                pivot1,pivot2 = L[1], L[0]
        if len(L) == 2:
                return [pivot1] + [pivot2]
        left, middle, right = [], [], []
        for num in L[2:]:
                if num < pivot1:
                        left.append(num)
                elif pivot1 <= num <= pivot2:
                        middle.append(num)
                else:
                        right.append(num)
        return dual_pivot_quicksort_copy(left) + [pivot1] + dual_pivot_quicksort_copy(middle) + dual_pivot_quicksort_copy(right)

#arr = create_random_list(100)
#dual_pivot_quicksort(arr)
#print(arr)
