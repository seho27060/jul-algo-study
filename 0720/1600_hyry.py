import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    Q = deque([(0, 0, 0, 0)])
    visit[0][0] = 0
    horse = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2))
    monk = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while Q:
        curR, curC, cost, curH = Q.popleft()

        if curR == R - 1 and curC == C - 1:
            return cost

        for dr, dc in horse:
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and \
                    (visit[newR][newC] > visit[curR][curC] + 1 or visit[newR][newC] == -1)\
                    and not MAP[newR][newC] and visit[curR][curC] < K:
                Q.append((newR, newC, cost + 1, curH + 1))
                visit[newR][newC] = visit[curR][curC] + 1

        for dr, dc in monk:
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and (visit[newR][newC] == -1 or visit[newR][newC] > visit[curR][curC])\
                    and not MAP[newR][newC]:
                Q.append((newR, newC, cost + 1, curH))
                visit[newR][newC] = visit[curR][curC]

    return -1


K = int(input())
C, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
visit = [[-1] * C for _ in range(R)]

print(bfs())