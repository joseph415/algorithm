import sys

sys.stdin = open("./9. 증가수열 만들기/in2.txt")

n = int(input())
List = list(map(int, input().split()))

lp = 0
rp = n - 1
res = []
temp = -1
while lp <= rp:
    if List[rp] < List[lp]:
        if temp < List[rp]:
            temp = List[rp]
            res.append('R')
            rp -= 1
        else:
            if temp < List[lp]:
                temp = List[lp]
                res.append('L')
                lp += 1
            else:
                break
    else:
        if temp < List[lp]:
            temp = List[lp]
            res.append('L')
            lp += 1
        else:
            if temp < List[rp]:
                temp = List[rp]
                res.append('R')
                rp -= 1
            else:
                break
print(len(res))
for i in res:
    print(i, end="")
