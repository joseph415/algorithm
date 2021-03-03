def solution(citations):
    answer = 0
    sortedCitations = sorted(citations)

    for i in range(len(sortedCitations)):
        h = len(sortedCitations) - i

        if i <= h <= sortedCitations[i] and h > answer:
            answer = h

    return answer

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer

if __name__ == '__main__':
    print(solution([0, 1, 4, 4, 6]))
