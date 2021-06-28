import sys

sys.stdin = open("../../섹션 8/1, 2. 네트워크 선 자르기/in5.txt")


def dp(n):
    f[1] = 1
    f[2] = 2

    for i in range(1, n - 1):
        f[i + 2] = f[i] + f[i + 1]

    print(f[n])


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    f = [0] * (n + 1)
    dp(n)
