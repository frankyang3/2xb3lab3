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
    if len(L) < 3:
        copy = L
        copy.sort()
        return copy
    x = [L[0], L[1]]
    x.sort()
    lp, rp = x[0], x[1]
    
    # x < lp, lp <= x <= rp, rp < x
    left, mid, right = [], [], []

    for num in L[2:]:
        if num < lp:
            left.append(num)
        elif num >= lp and num <= rp:
            mid.append(num)
        else:
            right.append(num)

    return dual_pivot_quicksort_copy(left) + [lp] + dual_pivot_quicksort_copy(mid) + [rp] + dual_pivot_quicksort_copy(right)
    
    
def tri_pivot_quicksort(L):
    copy = tri_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def tri_pivot_quicksort_copy(L):
        if len(L) < 4:
                copy = L
                copy.sort()
                return copy
        x = [L[0], L[1], L[2]]
        x.sort()
        pivot1, pivot2, pivot3 = x[0], x[1], x[2]
        left1, left2, right1, right2 = [], [], [], []
        for num in L[3:]:
                if num < pivot1:
                        left1.append(num)
                elif pivot1 <= num < pivot2:
                        left2.append(num)
                elif pivot2 <= num < pivot3:
                        right1.append(num)
                else:
                        right2.append(num)
        return tri_pivot_quicksort_copy(left1) + [pivot1] + tri_pivot_quicksort_copy(left2) + [pivot2] + tri_pivot_quicksort_copy(right1) + [pivot3] + tri_pivot_quicksort_copy(right2)

def quad_pivot_quicksort(L):
    copy = quad_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quad_pivot_quicksort_copy(L):
        if len(L) < 5:
                copy = L
                copy.sort()
                return copy
        x = [L[0], L[1], L[2], L[3]]
        x.sort()
        pivot1, pivot2, pivot3, pivot4 = x[0], x[1], x[2], x[3]
        left1, left2, right1, right2, right3 = [], [], [], [], []
        for num in L[4:]:
                if num < pivot1:
                        left1.append(num)
                elif pivot1 <= num < pivot2:
                        left2.append(num)
                elif pivot2 <= num < pivot3:
                        right1.append(num)
                elif pivot3 <= num < pivot4:
                        right2.append(num)
                else:
                        right3.append(num)
        return quad_pivot_quicksort_copy(left1) + [pivot1] + quad_pivot_quicksort_copy(left2) + [pivot2] + quad_pivot_quicksort_copy(right1) + [pivot3] + quad_pivot_quicksort_copy(right2) + [pivot4]+ quad_pivot_quicksort_copy(right3)
    
    
    
    
# Small lists functions
def selection_sort(arr):
    for i in range(len(arr)): 
        min_index = i 
        for j in range(i+1, len(arr)): 
            if arr[min_index] > arr[j]: 
                min_index = j 
                         
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr, l, h):
    for i in range(l + 1, h + 1):
        current = arr[i]
        j = i
        while j > l and arr[j - 1] > current:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = current
        

def final_sort(L, l, h):
    while l < h:
        if h < 10 + l:
            insertion_sort(L, l, h)
            break
        else:
            pivot = partition(L, l, h)
            final_sort(L, l, pivot - 1)
            l = pivot + 1
            final_sort(L, pivot + 1, h)
            h = pivot - 1

                
def partition(L, l, h):
    pivot = L[h]
    index = l
    for i in range(l, h):
        if L[i] <= pivot:
            L[i], L[index] = L[index], L[i]
            index += 1
            
    L[h], L[index] = L[index], L[h]
    return index
