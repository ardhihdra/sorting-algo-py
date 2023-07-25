import random

def quick_sort(arr):
    length = len(arr)
    if length <= 1 or (length == 2 and arr[0] <= arr[1]):
        return arr

    pivot_idx = random.randint(0, length-1)
    l_arr = [] * (length-1)
    r_arr = [] * (length-1)
    for x in range(length):
        if arr[x] <= arr[pivot_idx] and x != pivot_idx:
            l_arr.append(arr[x])
        elif arr[x] > arr[pivot_idx]:
            r_arr.append(arr[x])

    #print(l_arr, arr[pivot_idx], r_arr)
    sl_arr = quick_sort(l_arr)
    sr_arr = quick_sort(r_arr)
    return sl_arr + [arr[pivot_idx]] + sr_arr

#result = quicksort([2,3,24,2,42,2,32,3324,34,14,4,1,0])
#print('result: ', result)            
    
    
