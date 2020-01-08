import sys

sys.stdin = open("./3. 뮤직비디오/in6.txt", "rt")

m, n = map(int, input().split())
k = list(map(int, input().split()))

left = k[0]
right = sum(k)
cnt = 0
res = 0
while left <= right:
    cnt = 1
    rp = 0
    tot = 0
    mid = (left + right) // 2
    for i in range(m):
        if tot + k[i] > mid:
            cnt += 1
            tot = 0
        tot += k[i]
    if cnt <= n:
        res = mid
        right = mid - 1
    else:
        left = mid + 1
print(res)
