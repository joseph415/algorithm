import sys

sys.stdin = open("./3. 부분집합 구하기/in5.txt", "rt")

input_data = int(sys.stdin.readline(2))


# ans = []


# def DFS(n):
#     ans.append(n)
#     if n >= input_data:
#         return
#     else:
#         for j in range(n, input_data):
#             DFS(j + 1)
#             for k in ans:
#                 print(k, end=' ')
#             print()
#             ans.pop()
#
#
# if __name__ == '__main__':
#     for i in range(1, input_data + 1):
#         DFS(i)
#         print(ans.pop())

def DFS(v):
    if v == input_data + 1:
        for i in range(1, input_data + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


if __name__ == '__main__':
    ch = [0] * (input_data + 1)  # check point
    DFS(1)
