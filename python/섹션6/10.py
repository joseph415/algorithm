import sys
import collections
import itertools

sys.stdin = open("10. 조합 구하기/in1.txt", "rt")


# if __name__ == '__main__':
#     n, m = map(int, sys.stdin.readline().split())
#     list_ = [i for i in range(1, n + 1)]
#     print(list(itertools.combinations(list_, m)))


def DFS(index, start):
    global cnt

    if index == m:
        for j in range(index):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(start, n + 1):
            res[index] = i
            DFS(index + 1, i + 1)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    res = [0] * (n + 1)
    cnt = 0

    DFS(0, 1)
    print(cnt)
