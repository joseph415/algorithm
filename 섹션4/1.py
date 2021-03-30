import sys

sys.stdin = open("1. 이분검색/in5.txt", "rt")
n, target = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
l = 0
r = len(a) - 1
while l <= r:
    mid = (l + r) // 2

    if target == a[mid]:
        print(mid + 1)
        break
    elif target > a[mid]:
        l = mid + 1
    elif target < a[mid]:
        r = mid - 1
