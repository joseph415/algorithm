import sys

# 이분탐색응용
def main():
    global ans_

    left = 0
    right = len(a) - 1

    while True:
        mid = (left + right) // 2

        if len(a[left:right + 1]) == 2:
            ans_ += max(a[left:right])
            print(ans_)
            return

        ans_ += max(a[left:mid])

        left = mid + 1


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    ans_ = 0
    main()
