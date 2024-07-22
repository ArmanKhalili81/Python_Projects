from time import *
print("☼ Sequential Search ☼")


def seqsearch(ls1, n, x):
    location = 0
    while location < n and ls1[location] != x:
        location += 1

    if location < n:
        print(location)
    else:
        print('Does not exist !')


def main():
    ls = list(range(0,10000001))
    search_number = int(input("Enter A Number for To Search : "))
    start = time()
    seqsearch(ls,len(ls),search_number)
    print("{} Seconds " .format(time() - start))

if __name__ == '__main__':
    main()