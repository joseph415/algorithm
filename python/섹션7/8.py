import sys
from collections import deque

sys.stdin = open("../../섹션 7/8. 사과나무/in4.txt")


def BFS(start):
    global ans

    for i in range(n):
        ans += matrix[start][i]

    for count in range(1, start + 1):
        for k in range(count, n - count):
            ans += matrix[start - count][k]
            ans += matrix[start + count][k]


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    matrix = []
    ans = 0

    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    BFS(n // 2)
    print(ans)
