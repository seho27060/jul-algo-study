#220720 1600 말이 되고픈 원숭이
# 원숭원숭은 k번만 말의 이동가능
# 나머지는 상하좌우로 이동
# 시작점(0,0)에서 도착점(n-1,n-1)로 이동하는 동작의 최솟값 출력
# n <= 200, k <= 30
# 말이동한경우 /안한경우
# k*w*h 짜리 visited
import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global w, h, board, visited, monkey, horse,k
    queue = deque([])
    for idx in range(k):
        visited[idx][0][0] = [0,k]
    queue.append([0,0,0])

    while queue:
        nowR, nowC, dim = queue.popleft()
        #monkey
        for move in monkey:
            nxtR, nxtC = nowR + move[0], nowC + move[1]
            if 0 <= nxtR < h and 0 <= nxtC < w:
                if visited[dim][nxtR][nxtC][0] > visited[dim][nowR][nowC][0] + 1 and board[nxtR][nxtC] == 0:
                    visited[dim][nxtR][nxtC] = visited[dim][nowR][nowC].copy()
                    visited[dim][nxtR][nxtC][0] += 1
                    queue.append([nxtR,nxtC,dim])
        #horse
        if dim + 1 <= k:
            for move in horse:
                nxtR, nxtC = nowR + move[0], nowC + move[1]
                if 0 <= nxtR < h and 0 <= nxtC < w:
                    if visited[dim+1][nxtR][nxtC][0] > visited[dim][nowR][nowC][0] + 1 and board[nxtR][nxtC] == 0 and visited[dim][nowR][nowC][1] > 0:
                        visited[dim+1][nxtR][nxtC] = visited[dim][nowR][nowC].copy()
                        visited[dim + 1][nxtR][nxtC][0] += 1
                        visited[dim + 1][nxtR][nxtC][1] -= 1
                        queue.append([nxtR, nxtC, dim+1])
k = int(input())
w, h = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(h)]
visited = [[[[float('inf'),k] for _ in range(w)] for _ in range(h)] for _ in range(k+1)]
monkey = [[0,1],[0,-1],[1,0],[-1,0]]
horse = [[-2,1],[-1,2],[2,1],[1,2],[-2,-1],[-1,-2],[1,-2],[2,-1]]
# 원숭으로이동했을때[이동횟ㅐ수, 말이동횟수]/말로이동했을때[이동횟수, 말이동횟수]

bfs()

minV = float('inf')
# for kk in visited:
#     for jj in kk:
#         print(jj)
#     print()
for idx in range(k+1):
    if minV > visited[idx][-1][-1][0]:
        minV = visited[idx][-1][-1][0]
if minV >= float('inf'):
    print(-1)
else:
    print(minV)