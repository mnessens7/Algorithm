def buble_sort(a):
    n = len(a)
    for i in reversed(range(n)):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


a = [8, 4, 3, 9, 6]
buble_sort(a)
print(a)
