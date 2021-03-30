import sys
import math

sys.stdin = open("./8. 뒤집은 수/in1.txt", "rt")

# n = int(input())
#
# a = input().split()
#
#
# def reverse(x):
#     x = x[::-1]
#     return int(x)
#
#
# def prime(x):
#     if x != 1:
#         for i in range(2, x):
#             if x % i == 0:
#                 return False
#         return True
#
#
# for i in a:
#     if prime(reverse(i)):
#         print(reverse(i), end=' ')


# 풀이
n = int(input())

a = map(int, input().split())


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    # 1 자기자신 제외하면 절반까지만 존재
    # 루트 까지만 해도됨
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")

'''파이선스럽지 않은 코드'''
# def reverse(x):
#     x = ''.join(reversed((str(x))))
#     return int(x)
