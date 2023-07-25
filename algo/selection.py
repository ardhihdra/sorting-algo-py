def selection(int_input):
    #str_input = input('input comma separated: ')
    #int_input = [int(x) for x in str_input.split(',')]
    length = len(int_input)

    for x in range(length):
        smallest_idx = x
        for y in range(x, length):
            if int_input[y] < int_input[smallest_idx]:
                smallest_idx = y

        temp = int_input[x]
        int_input[x] = int_input[smallest_idx]
        int_input[smallest_idx] = temp

    return int_input

#selection()
