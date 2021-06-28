import sys

sys.stdin = open("./2. 쇠막대기/in5.txt", "rt")

n = input()
stack = []
res = 0
check = 0

for i in n:
    if i == '(':
        stack.append(i)
        check = 1
    else:
        stack.pop()
        if check == 1:
            res += len(stack)
        else:
            res += 1
        check = 2
print(res)
