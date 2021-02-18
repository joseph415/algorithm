import sys

sys.stdin = open("./10. 점수계산/in5.txt", "rt")

n = int(input())
tmp = input().split()
cnt = 0
S = 0
for i in tmp:
    if i == '1':
        cnt += 1
    else:
        cnt = 0
    S += cnt
print(S)
