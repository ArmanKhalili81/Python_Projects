from time import *


def fib(num):
    if num in {0, 1}:
        return num
    else:
        return fib(num-1) + fib(num-2)


def main():
    number = 30
    start = time()
    result_sum = fib(number)
    print("n : {0} -> {1} Seconds ".format(number, time() - start))
    print(result_sum)


if __name__ == '__main__':
    main()

#---------------------------------------------------------------#

def main_1():
    ls = []
    ls.extend({0, 1})
    start = time()
    for i in range(2, 150000):
        ls.append(ls[i-1] + ls[i-2])
    print("n : {0} -> {1} Seconds ".format(i, time() - start))
    print(ls.pop())


if __name__ == '__main__':
    main_1()
