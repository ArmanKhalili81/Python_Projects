print("☼ Exchange Sort ☼")
def exchange_sort(ls3, n):
    tmp = 0
    for i in range(n):
        for j in range(i+1, n):
            if ls3[i] > ls3[j]:
                tmp = ls3[i]
                ls3[i] = ls3[j]
                ls3[j] = tmp
    return ls3


def main():
    ls = [14, 90, 23, 45, 74, 36, 1, 55]
    result = exchange_sort(ls, len(ls))
    print(result)


if __name__ == '__main__':
    main()