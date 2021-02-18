import sys

sys.stdin = open("./4. 두 리스트 합치기/in1.txt", "rt")

# aSize = int(input())
# a = list(map(int, input().split()))
# bSize = int(input())
# b = list(map(int, input().split()))
#
# print(sorted(a+b))  //퀵소트라 nlogn

aSize = int(input())
a = list(map(int, input().split()))
bSize = int(input())
b = list(map(int, input().split()))  # 이미 정렬된 거 머지소트는 n 밖에 안걸림

p1 = p2 = 0
c = []
while p1 < aSize and p2 < bSize:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < aSize:
    c += a[p1:]
else:
    c += b[p2:]
print(c)
