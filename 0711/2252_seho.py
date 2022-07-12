#220712 2252 줄세우기
# n <= 32,000  m<=100,000
# 위상 정렬 , tc = O(v+e)

import sys
from collections import deque

input = sys.stdin.readline

def pologySort():
    result = []
    queue = deque()

    for i in range(1,n+1):
        if degree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for nxt in graph[now]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                queue.append(nxt)
    for res in result:
        print(res, end=" ")
n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1
pologySort()
