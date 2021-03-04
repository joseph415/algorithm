import math

numberHash = dict()
duplicated = dict()
N = 0
answer = 0


def determine(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def DFS(index, combination):
    global answer
    global N

    if index == N:
        if combination == "":
            return

        combination = int(combination)
        if determine(combination):
            if combination in duplicated:
                return

            duplicated[combination] = 1
            answer += 1
        return

    for i in numberHash:
        if numberHash[i] != 0:
            numberHash[i] -= 1
            DFS(index + 1, combination + i)
            numberHash[i] += 1
            DFS(index + 1, combination)

    return 0


def solution(numbers):
    global numberHash
    global N

    N = len(numbers)
    for i in numbers:
        if i not in numberHash:
            numberHash[i] = 0
        numberHash[i] += 1

    DFS(0, "")

    return answer

# from itertools import permutations
#
#
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         print(i, set(map(int, map("".join, permutations(list(n), i + 1)))))
#
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))  # 유니온 집합연산
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))  # 에라토스테네스 채 // 집합연산 위해서 set 지린다..
#     return len(a)


if __name__ == '__main__':
    print(solution("17"))
