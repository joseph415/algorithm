import sys

sys.stdin = open("2. 랜선자르기/in5.txt", "rt")

n, target = map(int, input().split())
k = [int(input()) for _ in range(n)]
k.sort()
Max = -2147000000
left = 0
right = n - 1
mid = (k[left] + k[right]) // 2
while left <= right:
    s = 0
    for i in range(n):
        s += k[i] // mid
    if s < target:
        right = mid - 1
        mid = (left + right) // 2
    elif s >= target:
        left = mid + 1
        mid = (left + right) // 2
print(mid)
