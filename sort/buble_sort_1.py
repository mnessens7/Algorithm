def buble_sort(a):
    for i in range(0, len(a)-1):
        modify_order(a, i)

def modify_order(a, i):
    for j in range(len(a)-1, i, -1):
        if a[j-1] > a[j]:
            a[j-1], a[j]=a[j], a[j-1]

a=[8, 4, 3, 9, 6]
buble_sort(a)
print(a)