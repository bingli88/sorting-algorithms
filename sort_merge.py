li = [5,4,3,2,1,9,21,45,78]
def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = len(x)/2
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result
print merge_sort(li)