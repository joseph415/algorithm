import math

# 피보나치에서 뒤의 0 개수구하기
def solution(n):
    answer = 0
    num = math.ceil(math.log(n, 5))

    for i in range(1, num + 1):
        answer += n // pow(5, i)

    return answer