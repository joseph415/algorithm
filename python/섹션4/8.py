import sys

sys.stdin = open("./8. 침몰하는 타이타닉/in4.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(n, m, a)
lp = 0
rp = 1
cnt = 0
while a:
    if len(a) == 1:
        cnt += 1
        a.pop()
        print(a)
        continue
    elif rp == len(a):
        cnt += 1
        a.pop(rp - 1)
        a.pop(lp)
        print(a)
        rp = 1
        continue
    else:
        if a[lp] + a[rp] <= m:
            rp += 1
        else:
            cnt += 1
            if rp - 1 != lp:
                a.pop(rp - 1)
                a.pop(lp)
            else:
                a.pop(lp)
            print(a)
            rp = 1
print(cnt)

