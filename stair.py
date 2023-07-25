def main():
    number = int(input('enter a number:'))

    for x in range(number):
        for y in range(x+1):
            print('#', end="")
        print('')
main()
