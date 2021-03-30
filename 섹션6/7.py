import sys
import math

sys.stdin = open("./7. 동전교환/in4.txt", "rt")


def knapSack(sum_, cnt):
    global min_

    if sum_ > target:
        return
    if cnt + math.ceil((target - sum_) / coin[0]) >= min_:
        return
    if sum_ == target:
        if min_ > cnt:
            min_ = cnt

    for i in coin:
        knapSack(sum_ + i, cnt + 1)


if __name__ == '__main__':
    n = sys.stdin.readline()
    coin = list(map(int, sys.stdin.readline().split()))
    coin.reverse()
    # coin.sort(reverse=True)
    target = int(sys.stdin.readline())
    min_ = 2714000000000

    knapSack(0, 0)
    print(min_)
