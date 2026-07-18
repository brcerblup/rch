import numpy as np
from math import fsum

reference_sum = fsum

def naive_sum(arr):
    summ = np.float64(0)
    for i in arr:
        summ += i
    return summ

def kahan_sum(arr):
    summ = np.float64(0)
    p = np.float64(0)
    for i in range(len(arr)):
        k = arr[i] - p
        l = summ + k
        p = (l-summ) - k
        summ = l
    return summ

def pairwise_sum(arr):
    if len(arr) == 0:
        return np.float64(0)
    elif len(arr) == 1:
        return np.float64(arr[0])
    else: 
        return pairwise_sum(arr[:len(arr)//2]) + pairwise_sum(arr[len(arr)//2:])
