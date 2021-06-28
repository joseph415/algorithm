# 미해결 문제 땅꽁문제
import sys


def main():
    global num
    global sm

    right = sm
    left = sm
    while True:
        if sm in a:
            ch[sm] = 1
        else:
            right += 1
            left -= 1


if __name__ == "__main__":
    peanutNum, EatingPeanut, sm = map(int, sys.stdin.readline().split())
    num = 0
    a = list(map(int, sys.stdin.readline().split()))
    ch = [0] * a[len(a) - 1]

    main()

# 6 3 7
# 2 4 5 8 11 12
