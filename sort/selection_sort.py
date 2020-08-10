def selection_sort(a):
    for i in range(0, len(a)-1):
        select_min(a, i)

def select_min(a, i):
    min = i
    for j in range(i+1, len(a)):
        if a[min] > a[j]:
            min = j
    a[i], a[min] = a[min], a[i]


a=[8, 4, 3, 9, 6]
selection_sort(a)
print(a)