import sys
import collections

sys.stdin = open("../../섹션 7/7. 송아지 찾기/in5.txt")


def BFS(n):
    queue = collections.deque()
    queue.append(n)

    while queue:
        pop = queue.popleft()

        if visit[pop] != 0 or pop <= 0:
            continue
        visit[pop] = 1

        for i in step:
            if pop + i == m:
                return depth[pop] + 1
            queue.append(pop + i)
            depth[pop + i] = depth[pop] + 1


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    step = [-1, 1, 5]
    visit = [0] * 10001
    depth = [0] * 10001
    ans = 0
    print(BFS(n))
