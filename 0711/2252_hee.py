from collections import deque
def bfs():
    ans = []
    Q = deque([])
    for i in range(1, N+1):
        if V[i] == 0:
            Q.append(i)

    while Q:
        n = Q.popleft()
        ans.append(n)
        for i in G[n]:
            V[i] -= 1
            if V[i] == 0:
                Q.append(i)

    return ans

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
V = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    V[B] += 1

print(*bfs())