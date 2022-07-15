import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
N, M, Q = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
sr, sc = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(M)]

def bfs(sr, sc):
    qu = deque()
    visited = [[-1] * N for _ in range(N)]
    qu.append([sr, sc])
    visited[sr][sc] = 0
    while qu:
        cr, cc = qu.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1 and G[nr][nc] != 1:
                qu.append([nr, nc])
                visited[nr][nc] = visited[cr][cc] + 1
    return visited

def check(visited, P):
    i = 0
    for sr, sc, nr, nc in P:
        P[i].append(visited[sr - 1][sc - 1])
        i += 1

    P.sort(key=lambda x: (-x[4], -x[0], -x[1]))


def goToHome(sr, sc):
    global Q
    while P:
        visited = bfs(sr - 1, sc - 1)
        check(visited, P)
        sr, sc, nr, nc, dist = P.pop()

        for p in P:
            p.pop()

        visited = bfs(sr - 1, sc - 1)
        dist2 = visited[nr - 1][nc - 1]
        sr, sc = nr, nc

        if dist == -1 or dist2 == -1:
            print(-1)
            return

        Q -= dist
        if Q < 0:
            break

        Q -= dist2
        if Q < 0:
            break

        Q += dist2 * 2

    if Q < 0:
        print(-1)
    else:
        print(Q)

goToHome(sr, sc)
