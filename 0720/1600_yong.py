# 3차원 배열을 활용한 bfs문제
# 말처럼 이동할 때 다른 배열로 옮겨 bfs를 진행

import sys
from collections import deque
input = sys.stdin.readline

hy = [2, 2, -2, -2, -1, -1, 1, 1]
hx = [1, -1, 1, -1, 2, -2, 2, -2]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*W for _ in range(H)] for _ in range(K+1)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1
while q:
    y, x, k = q.popleft()
    if y == H-1 and x == W-1:
        print(visited[k][y][x]-1)
        exit()
    if k < K:
        for h in range(8):
            ny = y + hy[h]
            nx = x + hx[h]
            if 0 <= ny < H and 0 <= nx < W:
                if arr[ny][nx] == 0 and visited[k+1][ny][nx] == 0:
                    visited[k+1][ny][nx] = visited[k][y][x] + 1
                    q.append((ny, nx, k+1))
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < H and 0 <= nx < W:
            if arr[ny][nx] == 0 and not visited[k][ny][nx]:
                visited[k][ny][nx] = visited[k][y][x] + 1
                q.append((ny, nx, k))

print(-1)