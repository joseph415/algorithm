import collections
import heapq


def solution(priorities, location):
    deque = collections.deque()
    maxHeap = []
    answer = 0

    for index, value in enumerate(priorities):
        deque.append([index, value])
        heapq.heappush(maxHeap, -value)

    highPriority = -heapq.heappop(maxHeap)

    while True:
        popleft = deque.popleft()

        if highPriority == popleft[1]:
            answer += 1
            if location == popleft[0]:
                return answer
            highPriority = -heapq.heappop(maxHeap)

        deque.append(popleft)


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
