import sys

sys.stdin = open("./3. k번째 큰 수/in5.txt", "rt")


def sol():
    a, b = map(int, input().split())
    List = sorted(list(map(int, input().split())))
    res = set()
    for i in range(a):
        for j in range(i + 1, a):
            for k in range(j + 1, a):
                res.add(List[i] + List[j] + List[k])
    res = sorted(res, reverse=True)
    print(res[b - 1])


if __name__ == '__main__':
    sol()
