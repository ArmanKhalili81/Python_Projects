from time import *

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
