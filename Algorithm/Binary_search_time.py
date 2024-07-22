from time import *
print("☼ Binary Search ☼")


def binary_search(ls1, n, x):
    location = 0
    low = 0
    high = n
    mid = 0
    while low <= high and location == 0:
        mid = (high+low)//2
        if x == ls1[mid]:
            location = mid
            print(location)
            return
        elif x < ls1[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print('Does not exist !')


def main():
    ls = list(range(0, 10000001))
    search_number = int(input("Enter A Number for To Search : "))
    start = time()
    binary_search(ls, len(ls), search_number)
    print("{} Seconds ".format(time() - start))


if __name__ == '__main__':
    main()