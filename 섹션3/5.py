import sys

sys.stdin = open("./5. 수들의 합/in5.txt", "rt")

a, b = map(int, input().split())
n = list(map(int, input().split()))
lt = 0
rt = 1
tot = n[lt]
cnt = 0
while lt <= rt:
    if tot < b:
        if rt < a:
            tot += n[rt]
            rt += 1
        else:
            break
        continue
    elif tot == b:
        cnt += 1
    tot -= n[lt]
    lt += 1
print(cnt)
