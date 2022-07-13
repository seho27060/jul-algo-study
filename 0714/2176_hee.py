from heapq import *
from collections import defaultdict
import sys
INF = sys.maxsize

input = sys.stdin.readline

def dijk():
    D[T] = 0
    V[T] = 1
    Q = [(0, T)]

    while Q:
        c, n1 = heappop(Q)

        if D[n1] < c:
            continue

        for cost, n2 in G[n1]:
            if D[n1] + cost < D[n2]:
                D[n2] = D[n1] + cost
                heappush(Q, (D[n2], n2))

            if D[n2] < c:
                V[n1] += V[n2]

N, M = map(int, input().split())
S, T = 1, 2

G = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))

D = [INF] * (N+1)
V = [0] * (N+1)

ans = 0
dijk()
print(V[S])