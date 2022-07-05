import sys
input = sys.stdin.readline
# from collections import deque


def find(x):
    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        childNum[root_x] += childNum[root_y]

T = int(input())
for _ in range(T):
    ans = 0
    F = int(input())
    parent = {}
    childNum = {}

    for _ in range(F):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            childNum[a] = 1

        if b not in parent:
            parent[b] = b
            childNum[b] = 1

        union(a, b)
        print(childNum[find(b)])
