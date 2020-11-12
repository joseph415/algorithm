import sys
from collections import deque

sys.stdin = open("./7. 교육과정 설계/in1.txt", "rt")
need = input()
n = int(input())

for i in range(n):
    dq = deque(need)
    target = deque(input())
    for x in target:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
