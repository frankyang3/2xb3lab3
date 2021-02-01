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

<<<<<<< HEAD
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

def quad_quicksort(L):
    copy = quicksort_copy_quad(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy_quad(L):
    if len(L) < 1:
        return []
    elif len(L) < 2:
        return L
    elif len(L) < 3:
        return [max(L[0], L[1]), min (L[0], L[1])]
    elif len(L) < 4:
        list.sort(L)
        return L
        
    pivotList = [L[0],L[1], L[2], L[3]]
    pivotList.sort()
    pivot1 = pivotList[0]
    pivot2 = pivotList[1]
    pivot3 = pivotList[2]
    pivot4 = pivotList[3]

    left, midleft, mid, midright, right = [], [], [], [], []
    for num in L[1:]:
        if num <= pivot1:
            left.append(num)
        elif num <= pivot2 and num > pivot1:
            midleft.append(num)
        elif num <= pivot3 and num > pivot2:
            mid.append(num)
        elif num <= pivot4 and num > pivot3:
            midright.append(num)
        elif num > pivot4:
            right.append(num)


    return quicksort_copy_quad(left) + [pivot1] + quicksort_copy_quad(midleft) + [pivot2] + quicksort_copy_quad(mid) + [pivot3] + quicksort_copy_quad(midright) + [pivot4] + quicksort_copy_quad(right)

arr = [1,20,20,30,15,1,2,3,5,25,35,45,60,57,37,217,17,16,18]
quad_quicksort(arr)
print(arr)

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
        for num in L[2:]:
                if num < pivot1:
                        left1.append(num)
                elif pivot1 <= num <= pivot2:
                        left2.append(num)
                elif pivot2 < num < pivot3:
                        right1.append(num)
                else:
                        right2.append(num)
        return tri_pivot_quicksort_copy(left1) + [pivot1] + tri_pivot_quicksort_copy(left2) + [pivot2] + tri_pivot_quicksort_copy(right1) + [pivot3] + tri_pivot_quicksort_copy(right2)
