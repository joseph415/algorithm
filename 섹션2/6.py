import sys

sys.stdin = open("./6. 자릿수의 합/in5.txt", "rt")


def digit_sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum


t = int(input())
n = input().split()
res = [digit_sum(i) for i in n]
Max = -2174000000
score = 0
for idx, x in enumerate(res):
    if Max < x:
        Max = x
        score = n[idx]

print(score)
