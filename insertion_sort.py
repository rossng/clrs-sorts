def insertion_sortw(A):
    A2 = list(A)
    return insertion_sort(A2)

def insertion_sort(A):
    for j in range(1, len(A)):
        # Get the next unsorted element
        key = A[j]
        i = j-1
        # Try each position in the sorted section, from high to low
        while i >= 0 and A[i] > key:
            # If key is still smaller, shift the array element to the right
            A[i+1] = A[i]
            i = i-1
        # When key is no longer smaller, insert it
        A[i+1] = key

    return A

arr1 = [5,2,4,6,1,3]
arr2 = [3,41,52,26,38,57,9,49]
            
