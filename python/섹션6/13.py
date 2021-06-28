import sys

sys.stdin = open("15. 경로탐색/in1.txt", "rt")


def initialAdjacency(list):
    adjacency = [[] for _ in range(n)]
    for i, j in list:
        adjacency[i - 1].append(j - 1)
    return adjacency


def DFS(start):
    global answer
    if start == n - 1:
        answer += 1
        print(path)
        return

    for i in range(len(adjacency[start]) - 1, -1, -1):
        pop = adjacency[start].pop(i)
        i_ = pop
        if visit[i_] == 0:
            visit[i_] = 1
            path.append(i_ + 1)
            DFS(i_)
            path.pop()
            visit[i_] = 0
        adjacency[start].append(pop)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    list_ = []
    visit = [0] * n
    answer = 0

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        list_.append([a, b])
    adjacency = initialAdjacency(list_)
    visit[0] = 1
    path = [1]
    DFS(0)
    print(answer)
