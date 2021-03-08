import sys
import collections
import itertools

sys.stdin = open("11. 수들의 조합/in5.txt", "rt")


def DFS(L, startIndex, sum):
    global cnt

    if L == k:
        if sum % m == 0:
            cnt += 1
        return
    for i in range(startIndex, n):
        DFS(L + 1, i + 1, sum + seq[i])


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    seq = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    cnt = 0

    DFS(0, 0, 0)
    print(cnt)
