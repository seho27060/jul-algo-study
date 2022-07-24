hx = [-1, -1, -2, -2, 1, 1, 2, 2]
hy = [-2, 2, -1, 1, -2, 2, -1, 1]

dx = [-1 ,1 , 0, 0]
dy = [0, 0, -1, 1]

k = int(input())
m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


def bfs(sx, sy, cnt):
    q = []
    q.append((sx, sy, cnt))
    v = [[[0 for _ in range(31)] for _ in range(m)] for _ in range(n)]
    v[sx][sy][0] = 1
    while q:
        cx, cy, ccnt = q.pop(0)
        if cx == n-1 and cy == m-1:
            return v[cx][cy][ccnt] - 1
        if ccnt < k:
            for i in range(8):
                nx = cx + hx[i]
                ny = cy + hy[i]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and v[nx][ny][ccnt+1] == 0:
                    q.append((nx, ny, ccnt+1))
                    v[nx][ny][ccnt+1] = v[cx][cy][ccnt] + 1

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and v[nx][ny][ccnt] == 0:
                q.append((nx, ny, ccnt))
                v[nx][ny][ccnt] = v[cx][cy][ccnt] + 1

    return -1

print(bfs(0, 0, 0))