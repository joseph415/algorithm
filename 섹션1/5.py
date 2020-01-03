import sys

sys.stdin = open("./5. 정다면체/in5.txt", "rt")

n, m = map(int, input().split())
cnt = [0] * (n + m)
max = -2147000000  # 4byte 가장작은수
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=' ')
