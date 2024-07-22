import math as m
N = 4


def queens(n):
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not(promising(i, j))) and (page[i][j] != 1):
                page[i][j] = 1
                if queens(n-1) == True:
                    return True
                page[i][j] = 0

    return False


def promising(i, j):
    for k in range(0, N):
        if page[i][k] == 1 or page[k][j] == 1:
            return True
    for k in range(0, N):
        for l in range(0, N):
            if (k+l == i+j) or (k-l == i-j):
                if page[k][l] == 1:
                    return True
    return False


page = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

queens(N)
for p in range(len(page)):
    print(page[p])