import sys

sys.stdin = open("./2. 숫자만 추출/in5.txt", "rt")

String = input()
temp = []
for i in String:
    """
    if i.decimal <-- 10진수(0~9)까지 이면 이고 digit는 그냥 숫자 2^32 4 이런거 전부
    if x.isdecimal():
        res=res*10+int(x)
    """
    if chr(48) <= i <= chr(57):
        temp.append(i)
res = int("".join(temp))
print(res)
count = 1
for i in range(2, res + 1):
    if res % i == 0:
        count += 1
print(count)


