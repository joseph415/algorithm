import sys

sys.stdin = open("./6. 격자판 최대합/in5.txt", "rt")

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

m = -2174000000

for i in range(n):
    sum2 = 0
    sum1 = sum(a[i])
    for j in range(n):
        sum2 += a[j][i]
    if m < sum2:
        m = sum2
    if m < sum1:
        m = sum1

# for i in range(n):
#     temp = 0
#     for j in range(n):
#         temp += a[j][i]
#     if m < temp:
#         m = temp

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - 1 - i]
    if m < sum2:
        m = sum2
    if m < sum1:
        m = sum1

print(m)
