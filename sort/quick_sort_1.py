def quick_sort(a):
    if len(a) < 2:
        return a
    p = a[0]
    x, y = divide(p, a[1:])
    return quick_sort(x)+[p]+quick_sort(y)


def divide(p, a):
    if len(a) < 1:
        return ([], [])
    x, y = divide(p, a[1:])
    aa = a[0]
    if aa < p:
        return ([aa]+x, y)
    else:
        return (x, [aa]+y)


a = [8, 4, 3, 9, 6]
c = quick_sort(a)
print(c)
