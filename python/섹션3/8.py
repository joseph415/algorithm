import sys

sys.stdin = open("./8. 곳감/in5.txt", "rt")

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

b = int(input())

c = [list(map(int, input().split())) for _ in range(b)]

for i in range(b):
    temp = a[c[i][0] - 1][:]
    # temp = list(a[c[i][0]-1)
    if c[i][1] == 0:
        for j in range(n):
            a[c[i][0] - 1][(j - c[i][2]) % n] = temp[j]
    else:
        for j in range(n):
            a[c[i][0] - 1][(j + c[i][2]) % n] = temp[j]

lp = 0
rp = n
mid = n // 2
s = 0
for i in range(n):
    for j in range(lp, rp):
        s += a[i][j]
    if i < mid:
        lp += 1
        rp -= 1
    else:
        lp -= 1
        rp += 1
print(s)
