import sys

sys.stdin = open("./9. 봉우리/in5.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    a[i].append(0)
    a[i].insert(0, 0)

temp = [0 for _ in range(len(a[0]))]
a.insert(0, temp)
a.append(temp)
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if a[i][j] > a[i - 1][j] and a[i][j] > a[i][j + 1] and a[i][j] > a[i + 1][j] and a[i][j] > a[i][j - 1]:
            cnt += 1
print(cnt)
