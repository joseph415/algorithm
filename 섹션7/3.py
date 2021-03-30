import sys

sys.stdin = open("../../섹션 7/3. 양팔저울/in5.txt", "rt")


def DFS(level, sum):
    if level == n:
        if sum > 0:
            res[sum - 1] = 1
        return

    DFS(level + 1, sum + list[level])
    DFS(level + 1, sum)
    DFS(level + 1, sum - list[level])


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    list = list(map(int, sys.stdin.readline().split()))
    total = sum(list)
    ans = 0

    res = [0] * total
    DFS(0, 0)
    for i in res:
        if i == 0:
            ans += 1
    print(ans)
