import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())
G = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

d = [0] * (n+1)
inf = 1e9


def dijk(s):
    q = []
    d[s] = inf
    heapq.heappush(q, (-inf, s))
    while q:
        cnt, now = heapq.heappop(q)
        cnt = -cnt
        for j in G[now]:
            cost = min(cnt,j[1])
            if d[j[0]] < cost:
                d[j[0]] = cost
                heapq.heappush(q, (-cost, j[0]))

dijk(s)
print(d[e])