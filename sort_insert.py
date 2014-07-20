li = [5,4,3,2,1]

def insertion_sort(li):
    for i in xrange(1,len(li)):
        elem = li[i]
        k = i - 1
        while k >= 0:
            if elem < li[k]:
                li[k+1] = li[k]
                li[k] = elem
                k = k - 1
            else:
                break
        print li
    return li
print insertion_sort(li)

