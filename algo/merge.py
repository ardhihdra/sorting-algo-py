def merge_sort(n):
    length = len(n)
    if length == 1:
        return n
    
    is_odd = length % 2 != 0
    mid = int(length / 2) if not is_odd else (length // 2) + 1
    mid = 1 + (length - 1)//2

    left = n[0:mid]
    right = n[mid:length]
    sleft = merge_sort(left)
    sright = merge_sort(right)
    lidx = 0
    ridx = 0
    new_arr = []
    for x in sleft + sright:
        value = 0
        if lidx >= len(sleft):
            value = sright[ridx]
            ridx += 1
        elif ridx >= len(sright):
            value = sleft[lidx]
            lidx += 1
        elif sleft[lidx] <= sright[ridx]:
            value = sleft[lidx]
            lidx += 1
        else:
            value = sright[ridx]
            ridx += 1
        new_arr.append(value)

    return new_arr

#arr = [int(x) for x in input("input numbers: ").split(',')]

#print(merge_sort(arr))

