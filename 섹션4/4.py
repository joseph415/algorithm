n = int(input())
a = input()
b = [0] * n

for i in range(n):
    b[i] = int(input())

res = 0
stack = []
for x in a:
    if x.isalpha():
        stack.append(b[ord(x)-ord('A')])
    else:
        temp2 = stack.pop()
        temp1 = stack.pop()
        if x == '+':
            stack.append(temp1 + temp2)
        elif x == '-':
            stack.append(temp1 - temp2)
        elif x == '*':
            stack.append(temp1 * temp2)
        elif x == '/':
            stack.append(temp1 / temp2)
print(f'{stack.pop():.2f}')
