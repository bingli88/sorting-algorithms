li = [5,4,6,3,2,45,8,1]
def selection_sort(li):
    for i in xrange(len(li)):
        mini = min(li[i:])
        mini_index = li.index(mini)
        li[mini_index], li[i] = li[i],li[mini_index]
    return li

print selection_sort(li)