import sys

sys.stdin = open("./5. 회의실 배정/in6.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x[1], x[0]))
cnt = 0
et = 0
for s, e in a:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
