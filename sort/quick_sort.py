def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[0]

    right = []
    left = []

    for i in range(1, n):
        if a[i] <= pivot:
            left.append(a[i])
        else:
            right.append(a[i])

    r= quick_sort(right)
    l= quick_sort(left)
    return l + [pivot] + r


a= [8, 4, 3, 9, 6]
c= quick_sort(a)
print(c)
