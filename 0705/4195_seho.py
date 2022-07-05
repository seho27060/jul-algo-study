#220705 4195 친구 네트워크
# 친구 관계 100,000
# 그래프? 유니온파인드?

import sys
input = sys.stdin.readline

def find(x):
    global parent
    if x == parent[x]:
        return x
    else:
        root = find(parent[x])
        parent[x] = root
        return parent[x]

def union(x,y):
    global answer, parent

    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        parent[rootY] = rootX
        answer[rootX] += answer[rootY]

tc_num = int(input())

for tc in range(tc_num):
    n = int(input())
    parent = dict()
    answer = dict()

    for _ in range(n):
        a, b = input().rstrip().split()

        if a not in parent:
            parent[a] = a
            answer[a] = 1
        if b not in parent:
            parent[b] = b
            answer[b] = 1

        union(a,b)
        print(answer[find(a)])