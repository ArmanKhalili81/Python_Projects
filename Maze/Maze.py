import Stack
Maze = [[0, 0, 0, 0, 9 ,0 ,0 ,0 ,0],
        [0, 9, 9, 0, 9 ,0 ,0 ,0 ,0],
        [0, 9, 0, 9, 0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 9, 0 ,0 ,100 ,0 ,0],
        [9, 0, 9, 0, 0 ,0 ,9 ,0 ,9],
        [0, 0, 0, 9, 0 ,0 ,0 ,0 ,0],
        [0, 9, 0, 0, 0 ,0 ,0 ,9 ,9]
        ]

table = [[0, 0, 0, 0, 0 ,0, 0, 0, 0],
         [0, 0, 0, 0, 0 ,0, 0, 0, 0],
         [0, 0, 0, 0, 0 ,0, 0, 0, 0],
         [0, 0, 0, 0, 0 ,0, 0, 0, 0],
         [0, 0, 0, 0, 0 ,0, 0, 0, 0],
         [0, 0, 0, 0, 0 ,0, 0, 0, 0],
         [0, 0, 0, 0, 0 ,0, 0, 0, 0]
         ]

ls = []

st = Stack()
x = 0
y = 0

st.push((x, y))
while Maze[x][y] != 100:
    if Maze[x][y] == 0:
        Maze[x][y] = 1
        # -----------------------------Check the last house-----------------------------------
        if x == len(Maze)-1 and y == len(Maze[0])-1:
            if Maze[x-1][y] == 0 or Maze[x-1][y] == 100:  # Up
                if Maze[x-1][y] == 0:
                    Maze[x-1][y] = 1
                st.push((x-1, y))
                x -= 1
                continue
            elif Maze[x][y-1] == 0 or Maze[x-1][y] == 100:  # Left
                if Maze[x][y-1] == 0:
                    Maze[x][y] = 1
                st.push((x, y-1))
                y -= 1
                continue
        # -----------------------------Check the last house-----------------------------------
        if y < len(Maze[0])-1 and (Maze[x][y+1] == 0 or Maze[x][y+1] == 100):  # Right
            st.push((x, y+1))
            y += 1
            continue
        elif x < len(Maze)-1 and (Maze[x+1][y] == 0 or Maze[x+1][y] == 100):  # Down
            st.push((x+1, y))
            x += 1
            continue
        elif x >= 1 and (Maze[x-1][y] == 0 or Maze[x-1][y] == 100):  # Up
            st.push((x-1, y))
            x -= 1
            continue
        elif y >= 1 and (Maze[x][y-1] == 0 or Maze[x][y-1] == 100):  # Left
            st.push((x, y-1))
            y -= 1
            continue
        Maze[x][y] = 2
        st.pop()
        x, y = st.peek()
    # ------------------ If One Of House Is 1 -------------------
    elif Maze[x][y] == 1:
        if y < len(Maze[0])-1 and (Maze[x][y+1] == 0 or Maze[x][y+1] == 100):  # Right
            st.push((x, y+1))
            y += 1
            continue
        elif x < len(table[0]) and (Maze[x+1][y] == 0 or Maze[x+1][y] == 100):  # Down
            st.push((x+1, y))
            x += 1
            continue
        elif x >= 1 and (Maze[x-1][y] == 0 or Maze[x-1][y] == 100):  # Up
            st.push((x-1, y))
            x -= 1
            continue
        elif y >= 1 and (Maze[x][y-1] == 0 or Maze[x][y-1] == 100):  # Left
            st.push((x, y-1))
            y -= 1
            continue
        Maze[x][y] = 2
        st.pop()
        x, y = st.peek()
#-------------------------------------------Motion Map-----------------------------------------------
for i in range(len(Maze)):
    for j in range(len(Maze[0])):
        if Maze[i][j] == 1:
            table[i][j] = '🐰'
        elif Maze[i][j] == 100:
            table[i][j] = '🥕'
        else:
            table[i][j] = '⛔'
#------------------------------------Coordinates Of Motion------------------------------------------------------
while st.size != 0:
    row, col = st.pop()
    ls.append((row, col))
#------------------------------------------------------------------------------------------
ls.reverse()
print("Coordinates Of Motion : ")
print(ls)
print('\n')
print("Motion Map :")
for i in range(len(table)):
    print(table[i])