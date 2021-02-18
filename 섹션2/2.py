import sys

sys.stdin = open("./2. k번째 작은수/in5.txt", "rt")


def sol():
    t = int(input())
    for i in range(t):
        n, s, e, k = map(int, input().split())
        List = list(map(int, input().split()))
        List = sorted(List[s-1:e])
        print("#" + str(i + 1) + " " + str(List[k - 1]))


if __name__ == '__main__':
    sol()
