import collections


def solution(people, limit):
    answer = 0
    people.sort()
    deque = collections.deque(people)

    while deque:
        if len(deque) == 1:
            answer += 1
            break

        first = deque.popleft()
        last = deque.pop()
        if first + last > limit:
            deque.appendleft(first)
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution([80, 70, 65, 65, 50], 120))
