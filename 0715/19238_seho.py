#220715 19238 스타트택시
# 구현?
# n < 20/ m < n^2
# 1) 현재자리에서 손님찾기
# 2) 가장가까운 손님에게 이동, 현재자리 갱신, 연료 갱신
# 3) 손님 데려다 주기, 현재자리 갱신, 연료 갱신
import sys
from collections import deque
from heapq import *
input = sys.stdin.readline

def goToCus(s):
    global n, fuel, board, customers, moves, end, start

    visited = [[float('inf')]*n for _ in range(n)]
    visited[s[0]][s[1]] = 0

    queue = deque([s])

    while queue:
        now = queue.popleft()

        for move in moves:
            nxtR, nxtC = now[0] + move[0], now[1] + move[1]
            if 0 <= nxtR < n and 0 <= nxtC < n:
                if board[nxtR][nxtC] == 0 and visited[nxtR][nxtC] > visited[now[0]][now[1]] + 1:
                    visited[nxtR][nxtC] = visited[now[0]][now[1]] + 1
                    queue.append([nxtR,nxtC])
    nxtCusLst = []
    # for kk in visited:
    #     print(kk)
    for cus in customers:
        cusR, cusC = cus[0]-1, cus[1] -1
        if fuel - visited[cusR][cusC] >= 0:
            heappush(nxtCusLst,([visited[cusR][cusC],cus]))

    if nxtCusLst:
        # print(nxtCusLst)
        dst, nxtCus = heappop(nxtCusLst)
        customers = [nxtCustomer for nxtCustomer in customers if nxtCustomer != nxtCus]
        nxtCus = [j-1 for j in nxtCus]
        fuel = fuel - visited[nxtCus[0]][nxtCus[1]]
        start = nxtCus[:2]
        end = nxtCus[2:]
        return True
    else:
        # print(start, fuel)
        return False

def goToEnd():
    global n, fuel, board, start, end, moves

    visited = [[float('inf')]*n for _ in range(n)]
    visited[start[0]][start[1]] = 0
    queue = deque([start])

    while queue:
        now = queue.popleft()

        for move in moves:
            nxtR, nxtC = now[0] + move[0], now[1] + move[1]
            if 0 <= nxtR < n and 0 <= nxtC < n:
                if board[nxtR][nxtC] == 0 and visited[nxtR][nxtC] > visited[now[0]][now[1]] + 1:
                    visited[nxtR][nxtC] = visited[now[0]][now[1]] + 1
                    queue.append([nxtR, nxtC])
    # for kk in visited:
    #     print(kk)
    if fuel - visited[end[0]][end[1]] >= 0:
        fuel += visited[end[0]][end[1]]
        start = end.copy()
        return True
    else:
        # print(start, end, fuel)
        return False
n, m, fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
start = list(map(int,input().split())); start = [start[0]-1,start[1]-1]
customers = [list(map(int,input().split())) for _ in range(m)]

moves = [[0,1],[0,-1],[1,0],[-1,0]]
# 업무시작
check = True
while customers:
# 승객 찾기
    end = []
    if goToCus(start): # 승객후보 찾았고
        if goToEnd():
            pass
        else:
            check = False
            break
    else:
        check = False
        break
if check:
    print(fuel)
else:
    print(-1)