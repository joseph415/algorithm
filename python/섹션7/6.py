import sys

sys.stdin = open("../../섹션 7/6. 알파코드/in4.txt")


def DFS(level, code):
    global cnt

    if level == length:
        cnt += 1
        print(code)
        return
    if int(codeList[level]) == 0:
        return

    if 1 <= int("".join(codeList[level:level + 1])) <= 26:
        DFS(level + 1, code + chr(int("".join(codeList[level:level + 1])) + 64))
    if level < length - 1 and 1 <= int("".join(codeList[level:level + 2])) <= 26:
        DFS(level + 2, code + chr(int("".join(codeList[level:level + 2])) + 64))


if __name__ == '__main__':
    n = sys.stdin.readline()
    codeList = list(n)
    length = len(codeList)
    cnt = 0
    DFS(0, "")
    print(cnt)
