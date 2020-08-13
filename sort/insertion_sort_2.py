def inseration_sort(a):
    n = len(a)
    for i in range(n):
        for j in reversed(range(i)):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            else:
                break


a = [8, 4, 3, 9, 6]
inseration_sort(a)
print(a)
