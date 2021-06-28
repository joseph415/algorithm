import sys
from collections import deque

sys.stdin = open("./8. 단어찾기/in5.txt", "rt")
n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for i in range(n - 1):
    word = input()
    p[word] = 0

for i in p:
    print(p[i])

for i in p.keys():
    if p[i] == 1:
        print(i)
        break
