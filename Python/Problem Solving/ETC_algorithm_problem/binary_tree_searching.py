def pre_order(tree, n):
    if n >= len(tree):
        return
    print(tree[n], end=' ')
    pre_order(tree, 2 * n)
    pre_order(tree, 2 * n + 1)


def in_order(tree, n):
    if n >= len(tree):
        return
    in_order(tree, 2 * n)
    print(tree[n], end=' ')
    in_order(tree, 2 * n + 1)


def post_order(tree, n):
    if n >= len(tree):
        return
    post_order(tree, 2 * n)
    post_order(tree, 2 * n + 1)
    print(tree[n], end=' ')


def solution():
    tree = [i for i in range(8)]
    print("pre_order")
    pre_order(tree, 1)
    print("\nin_order")
    in_order(tree, 1)
    print("\npost_order")
    post_order(tree, 1)


solution()
