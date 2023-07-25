def bubble_sort(arr_input):
    #str_input: str = input("Insert numbers separated by comma:")
    #arr_input: list[int] = [int(x) for x in str_input.split(',')]
    arr_len = len(arr_input)
    is_sorted = True

    for x in range(arr_len):
        for nx in range(arr_len-1):
            if arr_input[nx] > arr_input[nx+1]:
                temp = arr_input[nx+1]
                arr_input[nx+1] = arr_input[nx]
                arr_input[nx] = temp
                is_sorted = False
        # modified bubble sort
        if is_sorted:
            print('already sorted :)')
            break

    return arr_input

#bubble_sort()

