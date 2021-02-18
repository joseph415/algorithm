import sys

sys.stdin = open("./1. 재귀함수란(이진수출력)/in5.txt", "rt")

ans = []


def sol(n):
    if n % 2 == 0:
        ans.append("0")
    else:
        ans.append("1")
    if n < 2:
        return

    sol(n // 2)


a = int(sys.stdin.readline(1001))
sol(a)
for i in ans[::-1]:
    print(i, end="")
