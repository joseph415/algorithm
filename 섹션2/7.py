import sys
import math

sys.stdin = open("./7. 에라토스테네스 체/in5.txt", "rt")

N = int(input())
check = [False for i in range(N + 1)]
count = 0

for i in range(2, int(math.sqrt(N + 1)) + 1):
    for j in range(i+i, N + 1, i):
        check[j] = True

for i in range(2, N + 1):
    if not (check[i]):
        count += 1
print(count)

# for i in range(2, N + 1):
#     if not (check[i]):
#         count += 1
#         for j in range(i, N + 1, i):
#             check[j] = True
# print(count)
