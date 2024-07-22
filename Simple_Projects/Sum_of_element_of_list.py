print("☼ Sum ☼")
def sum(ls2, n):
    s = 0
    for i in range(n):
        s += ls2[i]
    return s


def main():
    ls = [10, 20, 30, 40, 50, 60, 70]
    result = sum(ls, len(ls))
    print(result)


if __name__ == '__main__':
    main()