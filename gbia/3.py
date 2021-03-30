import heapq

# 스케줄림
# 힙이용
# 시간을 뺴는것보다 더해나가자
def solution(N, coffee_times):
    answer = []
    temp = []
    priority = []

    for index, delay in enumerate(coffee_times):
        temp.append([delay, index])

    for i in range(N):
        heapq.heappush(priority, temp[i])

    index = N
    time = 0
    while priority:
        heappop = heapq.heappop(priority)
        time += heappop[0]
        answer.append(heappop[1] + 1)
        if index < len(coffee_times):
            heapq.heappush(priority, temp[index])
        for i in range(len(priority)):
            priority[i][0] += time
        index += 1

    return answer


# import collections
#
#
# def solution(N, coffee_times):
#     answer = []
#     deque = collections.deque()
#     for index, delay in enumerate(coffee_times):
#         deque.append([delay, index])
#
#     res = []
#     temp = []
#
#     while deque:
#         if len(res) < N:
#             res.append(deque.popleft())
#             continue
#
#         completedCoffee = min(res)[0]
#
#         for i in range(N):
#             res[i][0] -= completedCoffee
#             if res[i][0] == 0:
#                 answer.append(res[i][1] + 1)
#
#         for i in range(len(res)):
#             if res[i][0] != 0:
#                 temp.append([res[i][0], res[i][1]])
#
#         res.clear()
#         res = temp.copy()
#         temp.clear()
#
#     temp = []
#     while res:
#         if len(res) == 1:
#             answer.append(res[0][1] + 1)
#             return answer
#         completedCoffee = min(res)[0]
#
#         for i in range(len(res)):
#             res[i][0] -= completedCoffee
#             if res[i][0] == 0:
#                 answer.append(res[i][1] + 1)
#
#         for i in range(len(res)):
#             if res[i][0] != 0:
#                 temp.append([res[i][0], res[i][1]])
#         res.clear()
#         res = temp.copy()
#         temp.clear()
#
#     return answer


if __name__ == '__main__':
    print(solution(1, [100, 1, 2, 99, 4]))
