def pre_order(n):
    if n > 7:
        return
    else:
        print(n, end=' ')
        pre_order(n * 2)
        pre_order(n * 2 + 1)


def in_order(n):
    if n > 7:
        return
    else:
        in_order(n * 2)
        print(n, end=' ')
        in_order(n * 2 + 1)


def post_order(n):
    if n > 7:
        return
    else:
        post_order(n * 2)
        post_order(n * 2 + 1)
        print(n, end=' ')


if __name__ == '__main__':
    pre_order(1)
    print()
    in_order(1)
    print()
    post_order(1)