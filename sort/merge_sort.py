def merge_sort(a):
    if len(a) < 2:
        return a
    c = len(a) // 2
    return merge(merge_sort(a[:c]), merge_sort(a[c:]))


def merge(x, y):
    if len(x)<1:
        return y
    if len(y) <1:
        return x
    if (x[0] > y[0]):
        return [y[0]] + merge(x, y[1:])
    else:
        return [x[0]] + merge(x[1:], y)
print('Hello '+'')
print('Hello '+'world')


a=[8, 4, 3, 9, 6]
merge_sort(a)
print(a)