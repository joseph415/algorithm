def solution(citations):
    answer = 0
    sortedCitations = sorted(citations)

    for i in range(len(sortedCitations)):
        h = len(sortedCitations) - i

        if i <= h <= sortedCitations[i] and h > answer:
            answer = h

    return answer


if __name__ == '__main__':
    print(solution([0, 1, 3, 4, 6]))
