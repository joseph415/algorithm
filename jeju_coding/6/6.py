a = [[1, 0, 0, 0, 0],
     [0, 0, 1, 0, 1],
     [0, 0, 1, 0, 1],
     [0, 0, 1, 0, 1],
     [0, 0, 1, 0, 1]]

b = [[0, 0, 0, 0, 1],
     [0, 0, 0, 0, 3],
     [0, 0, 0, 0, 4],
     [0, 2, 0, 0, 2],
     [4, 5, 0, 2, 0]]

rotB = [[0 for _ in range(len(b))] for __ in range(len(b))]

for i in range(len(b)):
    for j in range(len(b)):
        rotB[i][j] = b[j][4 - i]

for i in range(len(b)):
    for j in range(len(b)):
        a[i][j] += rotB[i][j]

print([[chr(int("".join(str(i) for i in a[j]), 8))] for j in range(len(b))])
