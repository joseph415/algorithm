import math

matrix = []


def initMatrix(n, results):
    global matrix
    matrix = [[math.inf] * n for _ in range(n)]

    for win, loose in results:
        matrix[win - 1][loose - 1] = 1
        matrix[loose - 1][win - 1] = -1

    for i in range(n):
        matrix[i][i] = 0


# 내가 이긴 놈은 그놈이 이긴 사람 다 이기고, 그 사람은 내가 진놈 다져
def solution(n, results):
    if n == 1:
        return 1

    answer = 0
    initMatrix(n, results)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1 and matrix[i][k] == math.inf:
                        matrix[i][k] = 1
                        matrix[k][i] = -1
                    if matrix[i][k] == -1 and matrix[j][k] == math.inf:
                        matrix[j][k] = -1
                        matrix[k][j] = 1

    for i in matrix:
        print(i)

    for i in matrix:
        if math.inf not in i:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]))
