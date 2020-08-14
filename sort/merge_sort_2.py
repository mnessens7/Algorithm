def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        m = n//2
        left = a[:m]
        right = a[m:]
        return merge(merge_sort(left), merge_sort(right))


def merge(a, b):
    na = len(a)
    nb = len(b)
    i = 0
    j = 0
    c = []
    while i < na and j < nb:
        if b[j] < a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    while i < na:
        c.append(a[i])
        i += 1
    while j < nb:
        c.append(b[j])
        j += 1
    return c


a = [8, 4, 3, 9, 6]
c = merge_sort(a)
print(c)
