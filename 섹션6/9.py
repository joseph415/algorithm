import sys
import itertools

sys.stdin = open("9. 수열 추측하기/in5.txt", "rt")


# def pascal(tempList):
#     global target
#
#     temp = []
#     for i in range(len(tempList) - 1):
#         temp.append(tempList[i] + tempList[i + 1])
#     if len(temp) == 1:
#         if temp[0] == F:
#             print(target)
#             sys.exit(0)
#         return
#     pascal(temp)
#
#
# if __name__ == '__main__':
#     N, F = map(int, sys.stdin.readline().split())
#     l = [i for i in range(1, N + 1)]
#     permutations = list(itertools.permutations(l))
#     for i in permutations:
#         target = i
#         pascal(i)

def DFS(index, sum):
    if index == n and sum == F:
        for x in p:
            print(x, end=" ")
        exit(0)
    else:
        for k in range(1, n + 1):
            if ch[k] == 0:
                ch[k] = 1
                p[index] = k
                DFS(index + 1, sum + (b[index] * p[index]))
                ch[k] = 0


if __name__ == '__main__':
    n, F = map(int, sys.stdin.readline().split())
    p = [0] * n  # 순열
    b = [1] * n  # 이항계수
    ch = [0] * (n + 1)
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i  # 파스칼 조합 계수 공식
    DFS(0, 0)
