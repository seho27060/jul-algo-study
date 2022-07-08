import sys
input = sys.stdin.readline
# from collections import deque
from heapq import heappush, heappop

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

N = int(input())
qu = []
for i in range(1, N):
    arr = list(map(int, input().split()))
    for k in range(len(arr)):
        # print([arr[k], i, k + i + 1])
        heappush(qu, [arr[k], i, k + i + 1])
parent = [i for i in range(N + 1)]
nodes = [[] for _ in range(N + 1)]
while qu:
    dist, a, b = heappop(qu)

    if find(a) != find(b):
        union(a, b)
        nodes[a].append(b)
        nodes[b].append(a)

for i in nodes:
    i.sort()

for i in range(1, N + 1):
    print(len(nodes[i]), *nodes[i])
