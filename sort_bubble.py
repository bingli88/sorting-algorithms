li = [5,4,3,8,1,34,2,1]
                
def bubble_sort(li):      
    for a in range(len(li)):
        for b in range(len(li)-1):
            if (li[b+1] < li[b]):
                li[b+1], li[b] = li[b], li[b+1]
    return li
#print bubble_sort(li)
print bubble_sort(li)

def bubble_sort2(lst):
    for index in range(1,len(lst)):
        while index > 0 and lst[index-1] > lst[index]:
            lst[index-1] , lst[index] = lst[index] , lst[index-1]
            index -= 1