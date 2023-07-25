from datetime import datetime
import random

from algo.selection import selection
from algo.merge import merge_sort
from algo.bubble_sort import bubble_sort
from algo.quick_sort import quick_sort

arr_input = [int(x) for x in input('Input comma separated numbers, input 0 to use random value: ').split(',')]

if not arr_input[0]:
    arr_input = [random.randint(1, 10000) for _ in range(400)]


arr = arr_input.copy()
start = datetime.now()
print(merge_sort(arr))
print('merge sort finished in', datetime.now() - start)

print()

arr = arr_input.copy()
start = datetime.now()
print(selection(arr))
print('selectionsort finished in', datetime.now() - start)

print()

arr = arr_input.copy()
start = datetime.now()
print(bubble_sort(arr))
print('bubblesort finished in', datetime.now() - start)

print()

arr = arr_input.copy()
start = datetime.now()
print(quick_sort(arr))
print('quicksort finished in', datetime.now() - start)

