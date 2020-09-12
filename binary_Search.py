lst = [2,3,4,5,6,7]
pos = -1
def BinarySearch(lst,n):
    lst.sort()
    l = 0
    u = len(lst) -1
    while(l<=u):
        mid = (l+u)//2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid +1
            else :
                u = mid - 1
    return False
n=6
if BinarySearch(lst,n):
    print(f'Found at Index postion {pos}')
else:
    print("Not Found")