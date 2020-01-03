import sys

sys.stdin = open("./5. 정다면체/in5.txt", "rt")

a, b = map(int, input().split())

if a > b:
    for i in range(a - b + 1):
        print(b + i + 1, end=' ')
elif a <= b:
    for i in range(b - a + 1):
        print(a + i + 1, end=' ')
