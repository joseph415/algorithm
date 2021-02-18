import sys

sys.stdin = open("./4. 마구간 정하기/in5.txt", "rt")


def count(a, m):
    left = 0
    right = a[len(a) - 1] - a[0]
    res = 0
    while left <= right:
        cnt = 1
        cur = 0
        next = cur + 1
        mid = (left + right) // 2
        while next < len(a):
            if a[next] - a[cur] >= mid:
                cnt += 1
                cur = next
            next += 1
        if cnt < m:
            right = mid - 1
        else:
            left = mid + 1
            res = mid
    print(res)


n, m = map(int, input().split())

a = [int(input()) for _ in range(n)]

a.sort()
print(a)

count(a, m)
