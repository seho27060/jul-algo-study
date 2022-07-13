import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N + 1)
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    indegree[B] += 1

def topology_sort():
    res = []
    qu = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            qu.append(i)

    while qu:
        now = qu.popleft()
        res.append(now)

        for i in G[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                qu.append(i)
    for i in res:
        print(i, end=' ')

topology_sort()
