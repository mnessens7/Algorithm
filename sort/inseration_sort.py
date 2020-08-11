def inseration_sort(a):
    for i in range(1, len(a)):
        insert(a, i)

def insert(a, i):
    temp=a[i]
    for j in range(i-1, -1, -1):
        if temp<a[j]:
            a[j+1]=a[j]
        else:
            a[j+1]=temp
            break
    else:
        a[0]=temp


a=[8, 4, 3, 9, 6]
inseration_sort(a)
print(a)