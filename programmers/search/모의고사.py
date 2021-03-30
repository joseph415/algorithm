def solution(answers):
    answer = []
    one_count = 0
    two_count = 0
    three_count = 0

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if one[i % len(one)] == answers[i]:
            one_count += 1
        if two[i % len(two)] == answers[i]:
            two_count += 1
        if three[i % len(three)] == answers[i]:
            three_count += 1

    temp = [one_count, two_count, three_count]
    max_ = max(temp)

    for i in range(len(temp)):
        if temp[i] == max_:
            answer.append(i + 1)

    return answer

# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result



if __name__ == '__main__':
    print(solution([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
