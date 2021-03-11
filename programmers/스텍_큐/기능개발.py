import math
import collections


def solution(progresses, speeds):
    remainTimeRate = collections.deque()
    answer = []

    for i, j in zip(progresses, speeds):
        remainTimeRate.append(math.ceil((100 - i) / j))

    print(remainTimeRate)

    cnt = 1
    processingTime = remainTimeRate.popleft()

    while remainTimeRate:
        popleft = remainTimeRate.popleft()

        if popleft > processingTime:
            answer.append(cnt)
            cnt = 1
            processingTime = popleft
            continue
        cnt += 1

    # 마지막 처리
    answer.append(cnt)

    return answer


if __name__ == '__main__':
    print(solution([1, 99, 99], [100, 1, 1]))
