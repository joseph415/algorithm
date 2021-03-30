def f(n):
    if n <= 1:
        return 1
    else:
        return n + f(n - 1)


x = 0
n = 100

for i in range(1, 101):
    x += i

print(f(100))
