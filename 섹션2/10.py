import sys

sys.stdin = open("./10. 스도쿠 검사/in5.txt", "rt")

a = [list(map(int, input().split())) for _ in range(9)]

check_no = False

for i in range(9):
    check = [False for _ in range(9)]
    for j in range(9):
        if not (check[a[i][j] - 1]):
            check[a[i][j] - 1] = True
        else:
            check_no = True
            break
    if check_no:
        break

if not check_no:
    for i in range(9):
        check = [False for _ in range(9)]
        for j in range(9):
            if not (check[a[j][i] - 1]):
                check[a[j][i] - 1] = True
            else:
                check_no = True
                break
        if check_no:
            break

if not check_no:
    for l in range(3):
        for k in range(3):
            check = [False for _ in range(9)]
            for i in range(3):
                for j in range(3):
                    if not (check[a[i + 3 * l][j + 3 * k] - 1]):
                        check[a[i + 3 * l][j + 3 * k] - 1] = True
                    else:
                        check_no = True
                        break
                if check_no:
                    break
            if check_no:
                break
        if check_no:
            break

if check_no:
    print("No")
else:
    print("Yes")
