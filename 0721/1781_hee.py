from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
G = []
for _ in range(N):
    A, B = map(int, input().split())
    G.append((A, B))

G.sort()

Q = []
for dead, num in G:
    heappush(Q, num)
    if dead < len(Q):
        heappop(Q)
print(sum(Q))