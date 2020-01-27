import sys
from collections import deque

sys.stdin = open("./6. 응급실/in5.txt", "rt")
m, k = map(int, input().split())
# a = list(map(int, input().split()))
# List = [(a[i], i) for i in range(m)]

List = [i for i in enumerate(list(map(int, input().split())))]

d = deque(List)
cnt = 0

while True:
    temp = d.popleft()
    for i in d:
        if temp[1] < i[1]:
            d.append(temp)
            break
    else:
        cnt += 1
        if k == temp[0]:
            print(cnt)
            break
