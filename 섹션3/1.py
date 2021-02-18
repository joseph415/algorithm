import sys

sys.stdin = open("./1. 회문 문자열 검사/in1.txt", "rt")

n = int(input())

for i in range(n):
    s = input()
    if s.lower() == s[::-1].lower():
        print("#%d Yes" % (i + 1))
    else:
        print("#%d No" % (i + 1))
