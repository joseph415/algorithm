import sys

sys.stdin = open("./5. 바둑이 승차/in5.txt", "rt")


def DFS(index, sum_, predict):
    global max_

    if sum_ + (total - predict) < max_:
        return

    if c < sum_:
        return

    if index == n:
        if c >= sum_:
            if sum_ == c:
                print(c)
                exit(0)
            if max_ <= sum_:
                max_ = sum_
        return

    else:
        DFS(index + 1, sum_ + ba_duk[index], predict + ba_duk[index])
        DFS(index + 1, sum_, predict + ba_duk[index])


if __name__ == '__main__':
    c, n = map(int, sys.stdin.readline().split())
    ba_duk = []
    max_ = 0
    for i in range(n):
        ba_duk.append(int(sys.stdin.readline()))
    total = sum(ba_duk)
    DFS(0, 0, 0)
    print(max_)
