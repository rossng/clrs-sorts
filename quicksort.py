import random

def quicksortw(A, randomised=False):
    A2 = list(A)
    return randomised_quicksort(A2, 0, len(A2)-1) if randomised else quicksort(A2, 0, len(A2)-1)

def quicksort(A, p, r):
    if p < r:
        # Partition the array and return the position of the pivot
        q = partition(A, p, r)

        # Recursively quicksort each half of the array either side of the pivot
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A

def partition(A, p, r):
    # Get the pivot element
    x = A[r]
    # Elements with index : p <= index <= i are smaller than or equal to the pivot
    i = p-1

    # Loop through the as-yet unpartitioned elements
    for j in range(p, r):
        # If current element is smaller than the pivot
        if A[j] <= x:
            # Swap the element into the 'smaller than the pivot' section and
            # increment the upper boundary of that section
            i = i+1
            A[i], A[j] = A[j], A[i]

    # Finally, swap the pivot in place between the two sections and return its index        
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def randomised_quicksort(A, p, r):
    if p < r:
        q = randomised_partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A

def randomised_partition(A, p, r):
    # Before calling partition, swap a random element into the last position (i.e. the pivot)
    i = random.randrange(p, r+1)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

arr1 = [2,8,7,1,3,5,6,4]
arr2 = [13,19,9,5,12,8,7,4,21,2,6,11]
