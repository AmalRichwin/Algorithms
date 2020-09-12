def binary_search(arr,n):
    arr.sort()
    lower = 0
    upper = len(arr) - 1
    
    while(lower<=upper):
        mid = (lower+upper)//2
        if arr[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if arr[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1
    return False            

pos = -1    

arr = [2,5,8,3,9]

n = 6

if binary_search(arr,n):
    print(f'Found at Index Postion {pos}')
else:
    print('Not Found')

