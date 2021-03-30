import heapq


def solution(jobs):
    jobs.sort()
    answer = 0
    # time은 종료 시점
    time, candidates = 0, []

    for start, delay in jobs:
    # 작업완료 시간이후에 나온 time이므로 큐에 있는 작업들을 진행해 시간을 맞춰줌
        while start >= time:
            # 큐에 작업들이 존재하면 아직 시간을 맞추지 않은 것
            if candidates:
                d, s = heapq.heappop(candidates)
                answer += time - s + d
                time += d
            # 큐가 빌때가지 start가 time보다 이후에 나오는거면 그 사이 작업할 프로세스가 없는것
            else:
                time = start + delay
                answer += delay
                break
        # 시간을 마치는 도중에 start 가 time 이전에 실행되는 거면 다시 큐에 넣음
        else:
            heapq.heappush(candidates, [delay, start])

    while candidates:
        d, s = heapq.heappop(candidates)
        answer += time - s + d
        time += d

    return answer // len(jobs)


if __name__ == '__main__':
    print(solution([[1, 5], [2, 2], [2, 3]]))
