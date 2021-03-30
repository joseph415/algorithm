import sys

sys.stdin = open("../../섹션 7/5. 동전분배하기/in1.txt")


def DFS(level):
    global min_

    if level == n:
        sub = max(res) - min(res)
        if min_ > sub:
            if len(set(res)) == 3:
                min_ = sub
        return

    for i in range(3):
        res[i] += coin[level]
        if i == 0:
            a.append(coin[level])
        if i == 1:
            b.append(coin[level])
        if i == 2:
            c.append(coin[level])
        DFS(level + 1)
        res[i] -= coin[level]
        if i == 0:
            a.pop(a.index(coin[level]))
        if i == 1:
            b.pop(b.index(coin[level]))
        if i == 2:
            c.pop(c.index(coin[level]))


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    coin = []
    a = []
    b = []
    c = []
    res = [0] * 3
    min_ = 2147000000
    for _ in range(n):
        coin.append(int(sys.stdin.readline()))
    DFS(0)

    print(min_)
