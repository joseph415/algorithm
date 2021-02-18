import sys

sys.stdin = open("./3. 카드 역배치/in5.txt", "rt")

# digitList = [i for i in range(1, 21)]
#
# for i in range(10):
#     a, b = map(int, input().split())
#     temp = digitList[a - 1:b]
#     temp.reverse()
#     digitList[a - 1: b] = temp
# print(digitList)

"직접 바꾸기"
a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s) + 1 // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]

a.pop(0)
for x in a:
    print(x, end=' ')
