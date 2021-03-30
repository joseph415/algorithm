n = 0
set_ = set()
dict_ = dict()
string = ''

# 좋은 부분 순열 구하기
# zx, zx ,z 이렇게 중복되면 안됨
def DFS(level, partial):
    if level == n:
        return

    if dict_[string[level]] != 0:
        dict_[string[level]] = 0
        set_.add(partial + string[level])
        DFS(level + 1, partial + string[level])
        dict_[string[level]] = 1


def solution(s):
    global n
    global string

    string = s
    n = len(s)

    for i in range(n):
        if string[i] not in dict_:
            dict_[string[i]] = 1

    for i in range(n):
        DFS(i, '')

    return len(set_)


if __name__ == '__main__':
    print(solution("zxzxz"))
