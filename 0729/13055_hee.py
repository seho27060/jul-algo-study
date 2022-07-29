import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

def find(x):
    if x == P[x]:
        return x
    else:
        temp = find(P[x])
        P[x] = temp
        return P[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        P[b] = a

N, M = map(int, input().split())
S, E = map(int, input().split())
G = []
for _ in range(M):
    h1, h2, k = map(int, input().split())
    G.append((k, h1, h2))

G.sort(reverse=True)

P = [i for i in range(N + 1)]
T = [[] for _ in range(N + 1)]
for k, n1, n2 in G:
    if find(n1) != find(n2):
        union(n1, n2)
        T[n1].append((k, n2))
        T[n2].append((k, n1))

ST = deque([(INF, S)])
V = [False] * (N + 1)
V[S] = True
while ST:
    c, n1 = ST.popleft()

    if n1 == E:
        print(c)
        break

    for cost, n2 in T[n1]:
        if not V[n2]:
            V[n2] = True
            ST.append((min(cost, c), n2))
else:
    print(0)