import sys


def main():
    stack = []
    x = sys.stdin.readline()
    for i in range(len(x)):
        if stack:
            if stack[len(stack)-1] == x[i]:
                stack.append(x[i])
            else:
                stack.pop()
        else:
            stack.append(x[i])
    if stack:
        print("YES")
    else:
        print("No")


if __name__ == "__main__":
    main()