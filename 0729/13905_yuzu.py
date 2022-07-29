# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(1000)
#
# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
#
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a == b:
#         return
#     if rank[a] < rank[b]:
#         parent[b] = a
#     else:
#         parent[a] = b
#         if rank[a] == rank[b]:
#             rank[a] += 1
#
# def find(x):
#     if parent[x] == x:
#         return x
#     else:
#         parent[x] = find(parent[x])
#         return find(parent[x])
#
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# n, m = map(int, input().split())
# s, e = map(int, input().split())
# parent = [i for i in range(n+1)]
# rank = [0 for _ in range(n+1)]
#
# edges = []
# for _ in range(m):
#     h1, h2, k = map(int, input().split())
#     edges.append((k, h1, h2))
# edges.sort(reverse=True)
#
# def kruskal(edges):
#     ans = 1e9
#     for edge in edges:
#         k, h1, h2 = edge
#         if find(h1) != find(h2):
#             union(h1, h2)
#             ans = min(k, ans)
#         if parent[s] == parent[e]:
#             print(ans)
#             return
#     print(0)
#     return
#
# kruskal(edges)


import heapq
import sys
input = sys.stdin.readline
import collections

n, m = map(int, input().split())
s, e = map(int ,input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

snack = [0] * (n+1)
def dijkstra():
    q = [(-1e9, s)]
    snack[s] = 1e9
    while q:
        x, node = heapq.heappop(q)
        x = -x
        if snack[node] > x:
            continue
        for w, n in graph[node]:
            tmp = min(x, w)
            if snack[n] < tmp:
                snack[n] = tmp
                heapq.heappush(q, (-tmp, n))
dijkstra()
print(snack[e])