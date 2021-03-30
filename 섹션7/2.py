import sys

sys.stdin = open("../../섹션 7/2. 휴가/in1.txt", "rt")


def DFS(level, sum):
    global answer

    if level > n:
        return
    if level == n:
        if sum > answer:
            answer = sum
        return
    DFS(level + list[level][0], sum + list[level][1])
    DFS(level + 1, sum)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    list = []
    answer = -2147000000
    for i in range(n):
        T, P = map(int, sys.stdin.readline().split())
        list.append([T, P])

    print(list)
    DFS(0, 0)
    print(answer)
