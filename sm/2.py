import sys
import collections

# 피씨방
def main(key, index, sum_, cutEdge):
    global max_

    if sum_ + (total - cutEdge) < max_:
        return

    if sum_ > time:
        return

    if index == len(reverse[key]):
        if time >= sum_:
            if max_ <= sum_:
                max_ = sum_
        return
    else:
        main(key, index + 1, sum_ + reverse[key][index], cutEdge + reverse[key][index])
        main(key, index + 1, sum_, cutEdge + reverse[key][index])


if __name__ == "__main__":
    pcCounter, people, time = map(int, sys.stdin.readline().split())
    reverse = collections.defaultdict(list)

    for i in range(people):
        x, y = map(int, sys.stdin.readline().split())
        reverse[x].append(y)
    for i in reverse:
        reverse[i].sort(reverse=True)

    for i in reverse.keys():
        max_ = -2147000000
        total = sum(reverse[i])
        main(i, 0, 0, 0)
        print(i, max_ * 1000)


# 2 7 4
# 1 10
# 1 7
# 1 5
# 1 4
# 2 10
# 2 5
# 2 1