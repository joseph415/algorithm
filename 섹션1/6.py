import sys

sys.stdin = open("./6. 자릿수의 합/in5.txt", "rt")


def digit_sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum


t = int(input())
n = input().split()

print(n)
