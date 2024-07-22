print("☼ Maxtrix Multiple ☼")
ls1 = [
    [8, 14, -6],
    [12, 7, 4],
    [-11, 3, 21]]
ls2 = [
    [3, 16, -6],
    [9, 7, -4],
    [-1, 3, 13]]

ls3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(ls1)):
    for j in range(len(ls2)):
        ls3[i][j] = 0
        for k in range(len(ls3)):
            ls3[i][j] += ls1[i][k] * ls2[k][j]

for a in range(len(ls3)):
    print(ls3[a])