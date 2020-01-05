import sys

sys.stdin = open("./2. 숫자만 추출/in5.txt", "rt")

String = input()
temp = []
for i in String:
    if chr(48) <= i <= chr(57):
        temp.append(i)
res = int("".join(temp))
print(res)
count = 1
for i in range(2,res+1):
    if res%i == 0:
        count += 1
print(count)