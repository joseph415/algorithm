import sys

sys.stdin = open("./7. 사과나무/in5.txt", "rt")

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

mid = n // 2

lp = rp = mid
s = 0

for i in range(n):
    for j in range(lp, rp + 1):
        s += a[i][j]
    if i < mid:
        lp -= 1
        rp += 1
    else:
        lp += 1
        rp -= 1
print(s)
