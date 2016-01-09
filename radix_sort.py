from counting_sort import counting_sort

def string_radix_sortw(A):
    A2 = list(A)
    d = len(A2[0])
    return string_radix_sort(A2, d)

def string_radix_sort(A, d):
    """Perform a radix sort on a list A of uppercase strings of length d"""
    for i in reversed(range(0, d)):
        A = counting_sort(A, 26, lambda s: ord(s[i])-65)

    return A

arr1 = ['COW', 'DOG', 'SEA', 'RUG', 'ROW', 'MOB', 'BOX', 'TAB', 'BAR',
        'EAR', 'TAR', 'DIG', 'BIG', 'TEA', 'NOW', 'FOX']
