def selection_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if a[min] > a[j]:
                min = j
        tmp = a[min]
        a[min] = a[i]
        a[i] = tmp


a = [8, 4, 3, 9, 6]
selection_sort(a)
print(a)
