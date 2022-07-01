# DP문제
# 올 수 있는 값을 비교해 작은값을 가져온다.

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
DP = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i == 0:
            if arr[i][j] < arr[i][j-1]:
                DP[i][j] = DP[i][j-1]
            else:
                DP[i][j] = DP[i][j-1] + (arr[i][j] - arr[i][j-1]) + 1
        elif j == 0:
            if arr[i][j] < arr[i-1][j]:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] + (arr[i][j] - arr[i-1][j]) + 1
        else:
            val1 = val2 = 0
            if arr[i][j] < arr[i][j-1]:
                val1 = DP[i][j-1]
            else:
                val1 = DP[i][j-1] + (arr[i][j] - arr[i][j-1]) + 1
            if arr[i][j] < arr[i-1][j]:
                val2 = DP[i-1][j]
            else:
                val2 = DP[i-1][j] + (arr[i][j] - arr[i-1][j]) + 1
            DP[i][j] = min(val1, val2)

print(DP[n-1][n-1])