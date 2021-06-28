import sys

needs = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def solution(t):
    minDp[2] = "1"
    minDp[3] = "7"
    #
    # maxDp[2] = "1"
    # maxDp[3] = "7"
    #
    # tempMax = []
    # tempMin = []
    # for i in t:
    #     if maxDp[i] == "-1":
    #         for k in range(4, i + 1):
    #             tempMax.clear()
    #             tempMin.clear()
    #             for j in range(2, k - 1):
    #                 tempMax.append(int(maxDp[j] + maxDp[k - j]))
    #                 if k in needs:
    #                     minDp[k] = str(needs.index(k))
    #                 else:
    #                     if minDp[j] == "0":
    #                         tempMin.append(int("6" + minDp[k - j]))
    #                         continue
    #                     tempMin.append(int(minDp[j] + minDp[k - j]))
    #
    #             if tempMin:
    #                 tempMin.sort()
    #                 minDp[k] = str(tempMin[0])
    #             tempMax.sort(reverse=True)
    #             maxDp[k] = str(tempMax[0])
    tempMin = []
    for k in range(4, 101):
        tempMin.clear()
        for j in range(2, k - 1):
            if k in needs:
                minDp[k] = str(needs.index(k))
            else:
                if minDp[j] == "0":
                    tempMin.append(int("6" + minDp[k - j]))
                    continue
                tempMin.append(int(minDp[j] + minDp[k - j]))

        if tempMin:
            minDp[k] = str(min(tempMin))

    for i in t:
        max_num = ''
        if i % 2 == 0:
            max_num += '1' * (i // 2)
        else:
            max_num += '7'
            max_num += '1' * ((i - 3) // 2)
        maxDp[i] = max_num

        if i == 6:
            sys.stdout.writelines(f'{6} {maxDp[i]}\n')
        else:
            sys.stdout.writelines(f'{minDp[i]} {maxDp[i]}\n')
    # print(minDp)
    # print(maxDp)


if __name__ == '__main__':
    minDp = ["-1"] * 101
    maxDp = ["-1"] * 101
    n = int(sys.stdin.readline())
    t = []

    for i in range(n):
        t.append(int(sys.stdin.readline()))

    solution(t)
