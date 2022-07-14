import heapq
import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra():
    dp = [0]*(n+1)
    dp[2] = 1
    dist = [2147483647] * (n+1)
    dist[2] = 0
    q = [(0, 2)]
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for v, w in graph[node]:
            if d+w < dist[v]:
                dist[v] = d+w
                heapq.heappush(q, (d+w, v))
            if dist[v] > d:
                dp[v] += dp[node]
    print(dp[1])
    return

dijkstra()