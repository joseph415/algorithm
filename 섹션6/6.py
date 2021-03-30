import sys

sys.stdin = open("./6. 중복순열 구하기/in1.txt", "rt")


# if __name__ == '__main__':
#     n, m = map(int, sys.stdin.readline().split())
#     sequence = [i for i in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             print(i + 1, j + 1)
#
#     print(pow(n, m))

def DFS(level):
    global cnt
    if level == m:
        cnt += 1
        for i in res:
            if not i == 0:
                print(i, end=' ')
        print()
        return
    else:
        for i in range(1, n + 1):
            res[level] = i
            DFS(level + 1)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    res = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
