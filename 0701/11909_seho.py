# 220701 11909 배열 탈출
# 2차원 배열
# 각 격자에는 숫자가 배치, a -> b 이동할때, b의 값이 작아야함
# 각 격자의 숫자를 1 늘릴때마다 1원의 비용발생
# 돈을 가능한 적게 소비하면서
# 근데 마지막 행이나 마지막 열에 도달하면 행이동/ 열이동만 가능해짐

import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

visited = [[float('inf')]*n for _ in range(n)]
visited[0][0] = 0

moves = [[0,1],[1,0]]

for r in range(n):
    for c in range(n):
        for move in moves:
            nxtR, nxtC = r + move[0], c + move[1]
            if 0 <= nxtR < n and 0 <= nxtC < n:
                visited[nxtR][nxtC] = min(visited[nxtR][nxtC],
                                          visited[r][c] + max(board[nxtR][nxtC]-board[r][c]+1, 0))
print(visited[n-1][n-1])