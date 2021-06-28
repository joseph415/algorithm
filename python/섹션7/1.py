import sys

sys.stdin = open("../../섹션 7/1. 최대점수 구하기/in5.txt", "rt")


def DFS(level, sum, time):
    global answer

    if time > m:
        return

    if level == n:
        if answer < sum:
            answer = sum
        return

    DFS(level + 1, sum + question[level][0], time + question[level][1])
    DFS(level + 1, sum, time)


if __name__ == '__main__':
    answer = - 2147000000
    n, m = map(int, sys.stdin.readline().split())
    question = []
    totalSum = 0

    for _ in range(n):
        score, time = map(int, sys.stdin.readline().split())
        totalSum += time
        question.append([score, time])

    DFS(0, 0, 0)
    print(answer)
