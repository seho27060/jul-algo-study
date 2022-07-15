
import sys
from collections import deque
input = sys.stdin.readline


def findPerson(row, col):
    Q = deque([(row, col)])
    visit = [[0] * N for _ in range(N)]
    visit[row][col] = 1
    minDist = 1e10
    minR = minC = -1

    while Q:
        curR, curC = Q.popleft()
        if MAP[curR][curC] == 'S':
            if minDist > visit[curR][curC] - 1:
                minDist = visit[curR][curC] - 1
                minR, minC = curR, curC
            elif minDist == visit[curR][curC] - 1:
                if minR > curR:
                    minR, minC = curR, curC
                elif minR == curR:
                    if minC > curC:
                        minR, minC = curR, curC

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < N and 0 <= newC < N and not visit[newR][newC]\
                and MAP[newR][newC] != '1':
                Q.append((newR, newC))
                visit[newR][newC] = visit[curR][curC] + 1

    MAP[minR][minC] = '0'
    return minR, minC, minDist


def findGoal(pR, pC, gR, gC):
    Q = deque([(pR, pC)])
    visit = [[0] * N for _ in range(N)]
    visit[pR][pC] = 1

    while Q:
        curR, curC = Q.popleft()
        if (curR, curC) == (gR, gC):
            return visit[curR][curC] - 1

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < N and 0 <= newC < N and not visit[newR][newC] and\
                MAP[newR][newC] != '1':
                Q.append((newR, newC))
                visit[newR][newC] = visit[curR][curC] + 1

    return 1e10


def solution():
    global F, sR, sC

    cnt = 0

    while F > 0 and cnt < M:
        personR, personC, toPersonDist = findPerson(sR, sC)

        if F < toPersonDist:
            return -1
        F -= toPersonDist
        goalR, goalC = links[(personR, personC)]
        toGoalDist = findGoal(personR, personC, goalR, goalC)

        if F < toGoalDist:
            return -1
        cnt += 1
        F += toGoalDist
        sR, sC = goalR, goalC
        if cnt == M:
            return F
    return -1


N, M, F = map(int, input().split())
MAP = [list(input().split()) for _ in range(N)]

sR, sC = map(int, input().split())
sR -= 1
sC -= 1

links = dict()
for _ in range(M):
    a, b, c, d = map(int, input().split())
    links[(a - 1, b - 1)] = (c - 1, d - 1)
    MAP[a - 1][b - 1] = 'S'

print(solution())


'''
3 1 10
0 0 0
0 0 0
0 0 0
3 3
2 2 2 2
# 8

3 1 10
0 0 0
0 0 0
0 0 0
3 3
3 3 2 2
# 12

3 1 10
0 0 0
0 1 1
0 1 0
3 3
1 1 2 2
# - 1

3 1 10
0 0 0
0 1 1
0 1 0
3 3
3 3 3 3
# 10

3 2 10
0 0 0
0 0 0
0 0 0
3 3
2 2 1 1
1 1 2 2
# 12

3 9 100
0 0 0
0 0 0
0 0 0
3 3
1 1 2 2
1 2 2 2
1 3 2 2
2 1 2 2
2 2 2 3
2 3 2 2
3 1 2 2
3 2 2 2
3 3 2 2
# 104
'''