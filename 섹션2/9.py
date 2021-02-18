import sys

sys.stdin = open("./9. 주사위 게임/in5.txt", "rt")

# t = int(input())
# Max = 0
# while t > 0:
#     a = list(map(int, input().split()))
#     a.sort()
#     if a[0] == a[1] and a[1] == a[2]:
#         Sum = 10000 + a[0] * 1000
#     elif a[0] == a[1] or a[1] == a[2]:
#         Sum = 1000 + a[1] * 100
#     else:
#         Sum = max(a) * 100
#     if Max < Sum:
#         Max = Sum
#     t -= 1
#
# print(Max)

t = int(input())
Max = 0
for i in range(t):
    temp = input().split()
    temp.sort()
    a, b, c = map(int, temp)
    if a == b and b == c:
        Sum = 10000 + a * 1000
    elif a == b or a == c:
        Sum = 1000 + a * 100
    elif b == c:
        Sum = 1000 + b * 100
    else:
        Sum = max(a) * 100
    if Max < Sum:
        Max = Sum
print(Max)
