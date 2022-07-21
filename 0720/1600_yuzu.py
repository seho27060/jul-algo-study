from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

q = deque()
q.append((0, 0, k))
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
ans = -1
while q:
    x, y, j = q.popleft()
    if x == h-1 and y == w-1:
        ans = visited[x][y][j]
        break
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nx = x+dx
        ny = y+dy
        if 0<=nx<h and 0<=ny<w and arr[nx][ny] != 1 and visited[nx][ny][j] == 0:
            visited[nx][ny][j] = visited[x][y][j] + 1
            q.append((nx, ny, j))
    if j > 0:
        for dx, dy in ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)):
            nx = x+dx
            ny = y+dy
            if 0<=nx<h and 0<=ny<w and arr[nx][ny] != 1 and visited[nx][ny][j-1] == 0:
                visited[nx][ny][j-1] = visited[x][y][j] + 1
                q.append((nx, ny, j-1))
print(ans)