import sys

sys.stdin = open("../../섹션 8/1, 2. 네트워크 선 자르기/in5.txt")


def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if f[n] != 0:
        return f[n]
    f[n] = dp(n - 1) + dp(n - 2)

    return f[n]



if __name__ == '__main__':
    n = int(sys.stdin.readline())
    f = [0] * (n + 1)
    print(dp(n))
