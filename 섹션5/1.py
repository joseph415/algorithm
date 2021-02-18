import sys

sys.stdin = open("./1. 가장 큰 수/in6.txt", "rt")

n, m = map(str, input().split())
n = list(map(int, n))
m = int(m)
temp = 0
res = []
for i in range(len(n)):
    a = int(n[i])
    temp = a
    for j in res[::-1]:
        if j < a:
            res.pop()
            m -= 1
        if m == 0:
            break
    res.append(a)

    if m == 0:
        res = res + list(n[i + 1:])
        break
if m != 0:
    for i in res[:-m]:
        print(i, end="")
else:
    res = ''.join(map(str, res))
    print(res)
