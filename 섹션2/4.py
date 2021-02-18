import sys

sys.stdin = open("./4. 대표값/in1.txt", "rt")


def sol():
    t = int(input())
    List = list(map(int, input().split()))
    avg = round(sum(List) / t)
    temp = 21700000
    for idx, value in enumerate(List):
        if abs(value - avg) < temp:
            temp = abs(value - avg)
            score = value
            res = idx + 1
        elif abs(value - avg) == temp:
            if score < value:
                score = value
                res = idx + 1
    print(avg, res)


if __name__ == '__main__':
    sol()
