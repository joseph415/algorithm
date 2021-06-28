import sys

sys.stdin = open("./11. 격자판 회문수/in5.txt", "rt")
a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(7):
    lp = 0
    rp = 4
    while rp < 7:
        check1 = False
        check2 = False
        for j in range(5 // 2):
            if a[i][lp + j] != a[i][rp - j] and not check1:
                check1 = True
            if a[lp + j][i] != a[rp - j][i] and not check2:
                check2 = True
        if not check1:
            cnt += 1
        if not check2:
            cnt += 1
        lp += 1
        rp += 1

print(cnt)
