import sys

sys.stdin = open("./8. 순열 구하기/in4.txt", "rt")


def DFS(count, cutEdge):
    global ans
    if count + (N - cutEdge) < M:
        return
    if count > M:
        return

    if count == M:
        for i in ans_list:
            print(i, end=' ')
        ans += 1
        print()
        return

    for i in range(N):
        if i + 1 not in ans_list:
            ans_list.append(i + 1)
            DFS(count + 1, cutEdge + 1)
            ans_list.pop()


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    ans = 0
    ans_list = []
    sequence = [i for i in range(1, N + 1)]
    DFS(0, 0)
    print(ans)
