# 처음 필드에 승객인덱스를 표시
# bfs탐색을 통해 가장 가까운 승객 탐색
# 발견한 승객의 인덱스 정보로 도착점까지 이동하는 bfs함수 실행 

from collections import deque
import sys
input = sys.stdin.readline

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
def bfs1():
    global ty, tx
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    visited[ty][tx] = 0
    q.append((ty, tx))
    py = px = -1
    dis = 1000000000000
    while q:
        y, x = q.popleft()
        if f[y][x] > -1:
            if dis > visited[y][x]:
                dis = visited[y][x]
                py, px = y, x
            elif dis == visited[y][x]:
                if py > y:
                    dis = visited[y][x]
                    py, px = y, x
                elif py == y and px > x:
                    dis = visited[y][x]
                    py, px = y, x
        for dy, dx in d:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if f[ny][nx] != -1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
    if py == px == -1:
        return -1, -1
    else:
        idx = f[py][px]
        f[py][px] = -2
        ty, tx = py, px
        return idx, visited[py][px]


def bfs2(ey, ex):
    global ty, tx
    visited = [[0] * N for _ in range(N)]
    q = deque()
    visited[ty][tx] = 1
    q.append((ty, tx))
    while q:
        y, x = q.popleft()
        if y == ey and x == ex:
            ty, tx = y, x
            return visited[y][x] - 1
        for dy, dx in d:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if f[ny][nx] != -1 and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([y+dy, x+dx])
    return -1

N, M, O = map(int, input().split())
f = [list(map(int, input().split())) for _ in range(N)]
# 벽이면 -1, 아니면 -2
for i in range(N):
    for j in range(N):
        if f[i][j]:
            f[i][j] = -1
        else:
            f[i][j] = -2
ty, tx = map(int, input().split())
ty -= 1
tx -= 1

P = [[] for _ in range(M)]
G = [[] for _ in range(M)]
for i in range(M):
    sy, sx, ey, ex = map(int, input().split())
    f[sy-1][sx-1] = i
    P[i].append((sy-1, sx-1))
    G[i].append((ey-1, ex-1))

for _ in range(M):
    idx, move = bfs1()
    if idx == move == -1 or O - move <= 0:
        print(-1)
        exit()
    O -= move
    ey, ex = G[idx][0]
    value = bfs2(ey, ex)
    if value == -1 or O - value < 0:
        print(-1)
        exit()
    else:
        O += value
print(O)