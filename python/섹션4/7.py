import sys

sys.stdin = open("./7. 창고 정리/in5.txt", "rt")
height = int(input())
row = list(map(int, input().split()))
t = int(input())
row.sort()

while t > 0:
    row[height - 1] -= 1
    row[0] += 1
    t -= 1
    row.sort()
print(row[height-1] - row[0])
