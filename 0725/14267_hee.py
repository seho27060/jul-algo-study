from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
G = defaultdict(list)
for i in range(1, n):
    G[A[i]].append(i+1)

DP = [0] * (n+1)
for _ in range(m):
    i, w = map(int, input().split())
    DP[i] += w

V = [False] * (n+1)
Q = deque([1])
V[1] = True
while Q:
    n1 = Q.popleft()
    for n2 in G[n1]:
        if not V[n2]:
            V[n2] = True
            DP[n2] += DP[n1]
            Q.append(n2)

print(*DP[1:])
