import sys
from heapq import heappop, heappush
input = sys.stdin.readline
inf = sys.maxsize


def dijkstra():
    Q = [(0, 2)]
    dist[2] = 0
    memo[2] = 1

    while Q:
        cost, curV = heappop(Q)

        if dist[curV] < cost: continue

        for neiCost, neiV in adj[curV]:
            if dist[neiV] > dist[curV] + neiCost:
                dist[neiV] = dist[curV] + neiCost
                heappush(Q, (cost + neiCost, neiV))
            if cost > dist[neiV]:
                memo[curV] += memo[neiV]


V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    v1, v2, w = map(int, input().split())
    adj[v1].append((w, v2))
    adj[v2].append((w, v1))

dist = [inf] * (V + 1)
memo = [0] * (V + 1)
dijkstra()
minDist = dist[1]
print(memo[1])