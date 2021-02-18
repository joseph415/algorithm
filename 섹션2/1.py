import sys

sys.stdin = open("./섹션 1/1. k번째 약수/in4.txt", "rt")


def sol():
    a, k = map(int, input().split())  # string으로 읽은 문자 int로 변환

    idx = 0
    for i in range(1, a + 1):
        if (a % i) == 0:
            idx = idx + 1
        if idx == k:
            print(i)
            break
    else:
        print(-1)  # break 안하고 for문 정상끝나면 else안함 for else구문


if __name__ == '__main__':
    sol()
