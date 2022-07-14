# 다익스트라와 DP 알고리즘 문제
# 도착노드를 시작점으로 시작 노드까지 최단 거리를 구한다
# 구하는 중 다음 노드까지 거리가 현재 노드의 거리보다 크다면 DP값 갱신

import sys
import heapq
input = sys.stdin.readline

def dijk():
    D = [2147483647] * (N+1)
    q = []
    D[T] = 0
    heapq.heappush(q,(0, 2))
    while q:
        dis, now = heapq.heappop(q)
        if dis > D[now]:
            continue
        for n, v in G[now]:
            if D[n] > dis + v: 
                D[n] = dis + v
                heapq.heappush(q, (D[n], n))
            if D[n] > dis:
                DP[n] += DP[now]

S, T = 1, 2
ans = 0
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
DP = [0] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((B, C))
    G[B].append((A, C))
DP[T] = 1
dijk()
print(DP[S])