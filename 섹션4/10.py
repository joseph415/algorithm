import sys

sys.stdin = open("./10. 역수열/in5.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
res = [0] * n

for i in range(n):
    cnt = 0
    if i == 0:
        res[a[i]] = i + 1
        continue
    for j in range(n):
        if res[j] == 0 and a[i] != 0:
            cnt += 1
        if cnt == a[i]:
            if a[i] == 0:
                if res[j] == 0:
                    res[j] = i + 1
                    break
            else:
                if res[j + 1] == 0:
                    res[j + 1] = i + 1
                    break

for i in res:
    print(i, end=" ")
