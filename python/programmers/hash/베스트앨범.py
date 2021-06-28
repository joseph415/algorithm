import collections
import operator


def solution(genres, plays):
    answer = []
    hashMap = collections.defaultdict(dict)
    # orderedGeners = dict()
    orderedGeners = {g: 0 for g in set(genres)}

    for i in range(len(genres)):
        # if genres[i] not in orderedGeners:
        #     orderedGeners[genres[i]] = 0

        orderedGeners[genres[i]] += plays[i]
        hashMap[genres[i]][i] = plays[i]

    sortedGenreOrder = sorted(orderedGeners.items(), key=operator.itemgetter(1), reverse=True)

    for i in hashMap:
        hashMap[i] = dict(sorted(hashMap[i].items(), key=lambda x: (x[1], -x[0])))

    for i in sortedGenreOrder:
        if len(hashMap[i[0]]) < 2:
            answer.append(hashMap[i[0]].popitem()[0])
        else:
            answer.append(hashMap[i[0]].popitem()[0])
            answer.append(hashMap[i[0]].popitem()[0])

    # print(answer)
    return answer


# def solution(genres, plays):
#     answer = []
#     d = {e: [] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1], e[2]])
#         print(d)
#     genreSort = sorted(list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)
#     # print(genreSort)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
#         answer += temp[:min(len(temp), 2)]
#     return answer


if __name__ == '__main__':
    solution(["classic", "classic", "classic", "pop"], [500, 600, 600, 100])
