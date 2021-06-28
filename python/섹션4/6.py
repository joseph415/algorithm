import sys

sys.stdin = open("./6. 씨름선수/in5.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()
cnt = 0
for i in range(n):
    for j in range(n):
        height = a[i][0]
        weight = a[i][1]
        if height < a[j][0] and weight < a[j][1]:
            break
    else:
        cnt += 1
print(cnt)
