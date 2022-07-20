import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

Horse = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
Monkey = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def func():
    V[0][0][0] = 0
    Q = deque([(0, 0, 0, 0)]) # 거리, 말처럼 이동한 횟수, x, y

    while Q:
        cnt, num, x, y = Q.popleft()

        if x == W-1 and y == H-1:
            return V[y][x][num]
            
        if num < K:
            for dx, dy in Horse:
                nx = x + dx
                ny = y + dy
                if -1 < nx < W and -1 < ny < H and not G[ny][nx] and V[ny][nx][num+1] == -1:
                    V[ny][nx][num+1] = cnt + 1
                    Q.append((cnt+1, num+1, nx, ny))

        for dx, dy in Monkey:
            nx = x + dx
            ny = y + dy
            if -1 < nx < W and -1 < ny < H and not G[ny][nx] and V[ny][nx][num] == -1:
                V[ny][nx][num] = cnt + 1
                Q.append((cnt+1, num, nx, ny))
    return -1

K = int(input())
W, H = map(int, input().split())
G = []
for _ in range(H):
    G.append(list(map(int, input().split())))

V = [[[-1] * (K+1) for _ in range(W)] for _ in range(H)]
print(func())
