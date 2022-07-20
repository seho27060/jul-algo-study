import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import combinations

K = int(input())
W, H = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]

def f(sr, sc):
    qu = deque()
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    qu.append([sr, sc, 0])
    visited[sr][sc][0] = 1
    while qu:
        cr, cc, cnt = qu.popleft()

        if cr == H - 1 and cc == W - 1:
            return visited[cr][cc][cnt] - 1

        if cnt < K:
            for dr, dc in [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < H and 0 <= nc < W and visited[nr][nc][cnt + 1] == 0 and G[nr][nc] == 0:
                    qu.append([nr, nc, cnt + 1])
                    visited[nr][nc][cnt + 1] = visited[cr][cc][cnt] + 1
        for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < H and 0 <= nc < W and visited[nr][nc][cnt] == 0 and G[nr][nc] == 0:
                qu.append([nr, nc, cnt])
                visited[nr][nc][cnt] = visited[cr][cc][cnt] + 1
    return -1

ans = f(0, 0)
print(ans)
