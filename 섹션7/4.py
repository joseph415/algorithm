import sys

sys.stdin = open("../../섹션 7/4. 동전바꿔주기/in5.txt", "rt")


# def DFS(L, sum):
    # global cnt
    # if sum>m:
    #     return
    # if L==n:
    #     if sum==m:
    #         cnt+=1
    # else:
    #     for i in range(cn[L]+1):
    #         DFS(L+1, sum+(cv[L]*i))
def DFS(index, remainMoney):
    global answer

    if index == n or remainMoney < 0:
        return

    if remainMoney == 0:
        answer += 1
        return

    for i in range(index, n):
        if snap[i][1] == 0:
            continue
        else:
            snap[i][1] -= 1
            DFS(i, remainMoney - snap[i][0])
            snap[i][1] += 1


if __name__ == '__main__':
    # m = int(input())
    # n = int(input())
    # cv = list()
    # cn = list()
    # for i in range(n):
    #     a, b = map(int, input().split())
    #     cv.append(a)
    #     cn.append(b)
    # cnt = 0
    # DFS(0, 0)
    # print(cnt)
    money = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    snap = []
    answer = 0
    for _ in range(n):
        m, r = map(int, sys.stdin.readline().split())
        snap.append([m, r])

    snap.sort(reverse=True)

    DFS(0, money)
    print(answer)
