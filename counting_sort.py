def counting_sortw(A, get_key=lambda x: x):
    # get_key is a function that takes a list element and returns its key
    A2 = list(A)
    max_key = max([get_key(e) for e in A2])
    return counting_sort(A2, max_key, get_key)

def counting_sort(A, max_key, get_key):
    # All numbers in A are in the range 0, .. , k
    
    B = [None]*len(A)
    C = [0]*(max_key+1)

    # Populate C with the count of each element
    for i in range(0,len(A)):
        C[get_key(A[i])] += 1

    # Convert the counts in C to a cumulative sum
    for i in range(1,len(C)):
        C[i] += C[i-1]

    # Sort from A into B using the positions calculated in C
    for i in reversed(range(0, len(A))):
        B[C[get_key(A[i])]-1] = A[i]
        C[get_key(A[i])] -= 1

    return B

arr1 = [2,5,3,0,2,3,0,3]
arr2 = [6,0,2,0,1,3,4,6,1,3,2]
arr3 = [(2,'fred'),(5,'bob'),(3,'steve'),(0,'john'),(2,'gary')
        ,(3,'tarquin'),(0,'albert'),(3,'zeus')]
