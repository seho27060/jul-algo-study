import sys
input = sys.stdin.readline
# from collections import deque
from heapq import heappush, heappop

S, T = 1, 2
INF = 2147483647
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append([C, B])
    G[B].append([C, A])

# print(G)

# 합리적 이동경로 개수
dp = [0] * (N + 1)
dp[T] = 1
# 이동거리
dist = [INF] * (N + 1)
dist[T] = 0

qu = []
qu.append([0, T])

while qu:
    cur_dist, cur_node = heappop(qu)

    if cur_dist > dist[cur_node]:
        continue

    for new_dist, new_node in G[cur_node]:
        if dist[new_node] > cur_dist + new_dist:
            dist[new_node] = cur_dist + new_dist
            heappush(qu, [dist[new_node], new_node])
        if cur_dist > dist[new_node]:
            dp[cur_node] += dp[new_node]
print(dp[S])
