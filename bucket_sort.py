import math
import itertools

def bucket_sortw(A):
    A2 = list(A)
    return bucket_sort(A2)

def bucket_sort(A):
    """Sorts a list of numbers in the range [0,1)"""
    n = len(A)
    B = [[] for x in range(0,n)]
    for i in range(0,n):
        B[math.floor(n*A[i])].insert(0, A[i])
    for b in B:
        b.sort() # technically, we should probably use insertion sort
    return list(itertools.chain(*B))

arr1 = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
arr2 = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
