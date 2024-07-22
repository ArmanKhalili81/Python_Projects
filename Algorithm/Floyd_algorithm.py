# floyd
w = [[0,1,999,1,5],[9,0,3,2,999],[999,999,0,4,999],[999,999,2,0,3],[3,999,999,999,0]]
D = w
for k in range(len(D)):
    for i in range(len(D)):
        for j in range(len(D)):
            D[i][j] = min(D[i][j],D[i][k]+D[k][j])

for p in range(len(w)):
    print(D[p])

print()

# floyd_2
w = [[0,1,999,1,5],[9,0,3,2,999],[999,999,0,4,999],[999,999,2,0,3],[3,999,999,999,0]]
p = [[0,0,0,0,0]]*5
D = w
for k in range(len(D)):
    for i in range(len(D)):
        for j in range(len(D)):
            if D[i][k]+D[k][j] < D[i][j] :
                p[i][j] = k
                D[i][j] = D[i][k]+D[k][j]

