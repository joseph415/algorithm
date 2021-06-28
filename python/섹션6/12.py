import sys

sys.stdin = open("12/in.txt", "rt")


def initialAdjacency(list):
    adj = [[0 for _ in range(n)] for _ in range(n)]
    for i, j, d in list:
        adj[i - 1][j - 1] = d
    return adj


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    list = []
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        list.append([a, b, c])

    print(initialAdjacency(list))
