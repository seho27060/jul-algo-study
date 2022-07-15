import sys
from collections import deque
D = [(0, -1), (-1, 0), (1, 0), (0, 1)]
INF = sys.maxsize

def bfs(sx, sy):
    V[sy][sx] = 0
    Q = deque([(sx, sy)])
    while Q:
        x, y = Q.popleft()

        for dx, dy in D:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < N and V[ny][nx] == -1 and not G[ny][nx]:
                V[ny][nx] = V[y][x] + 1
                Q.append((nx, ny))

N, M, O = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

y, x = map(int, input().split())
x, y = x-1, y-1

C = []
for i in range(M):
    sy, sx, ey, ex = map(int, input().split())
    C.append((sx-1, sy-1, ex-1, ey-1))
C.sort(key=lambda x: (x[1], x[0]), reverse=True)
visited = [False] * M

for _ in range(M):
    V = [[-1] * N for _ in range(N)]
    bfs(x, y)
    dist = INF
    num = 0
    for i in range(M):
        if not visited[i]:
            sx, sy, ex, ey = C[i]
            if -1 < V[sy][sx] and V[sy][sx] <= dist:
                dist = V[sy][sx]
                num = i

    sx, sy, ex, ey = C[num]
    visited[num] = True
    O -= dist

    V = [[-1] * N for _ in range(N)]
    bfs(sx, sy)

    if V[ey][ex] < 0:
        print(-1)
        break

    O -= V[ey][ex]

    if O < 0:
        print(-1)
        break

    O += 2 * V[ey][ex]
    x, y = ex, ey

else:
    print(O)


