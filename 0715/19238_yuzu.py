from collections import deque
import sys
input = sys.stdin.readline

n, m, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tx, ty = map(int, input().split())
tx -= 1
ty -= 1
people = []

for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())
    people.append([sx-1, sy-1, ex-1, ey-1])
people.sort()

def dist(tx, ty):
    q = deque()
    q.append((tx, ty))
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[tx][ty] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited

def near(visited, people):
    minD = 1e9
    minIdx = -1
    for i in range(len(people)):
        sx, sy, ex, ey = people[i]
        if visited[sx][sy] < minD:
            minD = visited[sx][sy]
            minIdx = i
    return minIdx, minD

def solve(tx, ty):
    global fuel
    while people:
        visited = dist(tx, ty)
        minIdx, minD = near(visited, people)
        sx, sy, ex, ey = people[minIdx]
        del people[minIdx]

        drive = dist(sx, sy)
        tx, ty = ex, ey

        if minD == -1 or drive[ex][ey] == -1:
            return -1

        fuel -= minD
        if fuel < 0:
            return -1

        fuel -= drive[ex][ey]
        if fuel < 0:
            return -1

        fuel += drive[ex][ey]*2

    return fuel

print(solve(tx, ty))