from collections import deque
dx = [1, 0]
dy = [0, 1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    v[sx][sy][0] = 1
    while q:
        cx, cy = q.popleft()
        if cx == n-1 and cy == n-1:
            return v[cx][cy][1]
        for i in range(2):
            if cy != n-1 or cx != n-1:
                nx = cx + dx[i]
                ny = cy + dy[i]
            elif cy == n-1:
                nx = cx + 1
                ny = cy
            elif cx == n-1:
                nx = cx
                ny = cy + 1
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny][0] == 0:
                v[nx][ny][0] = 1
                if arr[cx][cy] > arr[nx][ny]:
                    v[nx][ny][1] = v[cx][cy][1]
                    q.append((nx, ny))

                else:
                    v[nx][ny][1] = v[cx][cy][1] + arr[nx][ny] - arr[cx][cy] + 1
                    q.append((nx, ny))
            elif 0 <= nx < n and 0 <= ny < n and v[nx][ny][0] == 1:
                if arr[cx][cy] > arr[nx][ny] and v[cx][cy][1] < v[nx][ny][1]:
                    v[nx][ny][1] = v[cx][cy][1]
                    q.append((nx, ny))

                elif arr[cx][cy] <= arr[nx][ny] and v[nx][ny][1] > v[cx][cy][1] + arr[nx][ny] - arr[cx][cy] + 1:
                    v[nx][ny][1] = v[cx][cy][1] + arr[nx][ny] - arr[cx][cy] + 1
                    q.append((nx, ny))



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[[0] * 2 for _ in range(n)] for _ in range(n)]

bfs(0, 0)
print(v[n-1][n-1][1])