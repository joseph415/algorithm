import sys

sys.stdin = open("./5. 공주구하기/in5.txt", "rt")

n, k = map(int, input().split())
check = [0] * n
idx = 0
t = 0
cnt = 0
target = k - 1

while True:
    if check[idx % n] == 0:
        if t % k == target:
            check[idx % n] = -1
            cnt += 1
        idx += 1
        t += 1
    elif check[idx % n] == -1:
        idx += 1
    if n - cnt == 1:
        break

for i in check:
    if i != -1:
        print(check.index(i)+1)
        break
