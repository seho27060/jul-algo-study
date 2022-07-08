from heapq import *

N = int(input())

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
        return True

I = []
G = [[] for _ in range(N+1)]
P = [i for i in range(N+1)]
for i in range(1, N):
    L = list(map(int, input().split()))
    for j in range(N-i):
        heappush(I, (L[j], i, i+j+1))

while I:
    c, s, e = heappop(I)
    if union(s, e):
        G[s].append(e)
        G[e].append(s)

for i in range(1, N+1):
    G[i].sort()
    print(len(G[i]), end = ' ')
    for j in G[i]:
        print(j, end = ' ')
    print()



