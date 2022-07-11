import sys
from collections import deque
input = sys.stdin.readline


def topological():
    global Q
    visit = [False] * (N + 1)

    while Q:
        curV = Q.popleft()
        visit[curV] = True
        ans.append(curV)

        for neiV in adj[curV]:
            if not visit[neiV]:
                degree[neiV] -= 1
                if not degree[neiV]:
                    Q.append(neiV)


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    degree[B] += 1

Q = deque()
for idx in range(1, N + 1):
    if not degree[idx]:
        Q.append(idx)

ans = deque()
topological()
print(*ans)