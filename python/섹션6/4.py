import sys

sys.stdin = open("./4. 합이 같은 부분집합/in5.txt", "rt")


# inputData = int(sys.stdin.readline())
# inputList = list(map(int, sys.stdin.readline().split()))
#
#
# def DFS(index):
#     if index == inputData:
#         right = 0
#         left = 0
#         for i in range(inputData):
#             if cp[i] == 1:
#                 right += inputList[i]
#             else:
#                 left += inputList[i]
#         if right == left:
#             print("YES")
#             exit(0)
#         return
#     else:
#         cp[index] = 1
#         DFS(index + 1)
#         cp[index] = 0
#         DFS(index + 1)
#
#
# if __name__ == '__main__':
#     cp = [0] * (inputData + 1)
#     DFS(0)
#     print("NO")

# def DFS(index, sum):
#     if index == inputData:
#         if sum == (total - sum):  # 부분집합의 다른부분 합
#             print("YES")
#             sys.exit(0)
#         else:
#             DFS(index + 1, sum + inputList[index])
#             DFS(index + 1, sum)
#
#

def DFS(index, sum):
    if sum > total // 2:
        return
    if index == inputData:
        if sum == (total - sum):  # 부분집합의 다른부분 합
            print("YES")
            sys.exit(0)
        else:
            DFS(index + 1, sum + inputList[index])
            DFS(index + 1, sum)


if __name__ == '__main__':
    inputData = int(sys.stdin.readline())
    inputList = list(map(int, sys.stdin.readline().split()))
    total = sum(inputList)
    DFS(0, 0)
    print("NO")
