import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for k in range(N):
        if i == 0 and k == 0:
            continue
        elif i == 0:
            tmp = -1
            diff = G[i][k - 1] - G[i][k]
            if diff > 0:
                tmp = dp[i][k - 1]
            else:
                tmp = dp[i][k - 1] + (-diff) + 1
            dp[i][k] += tmp
        elif k == 0:
            tmp = -1
            diff = G[i - 1][k] - G[i][k]
            if diff > 0:
                tmp = dp[i - 1][k]
            else:
                tmp = dp[i - 1][k] + (-diff) + 1
            dp[i][k] += tmp
        else:
            tmp1, tmp2 = -1, -1
            diff1 = G[i - 1][k] - G[i][k]
            if diff1 > 0:
                tmp1 = dp[i - 1][k]
            else:
                tmp1 = dp[i - 1][k] + (-diff1) + 1

            diff2 = G[i][k - 1] - G[i][k]
            if diff2 > 0:
                tmp2 = dp[i][k - 1]
            else:
                tmp2 = dp[i][k - 1] + (-diff2) + 1
            dp[i][k] = min(tmp1, tmp2)
print(dp[N - 1][N - 1])
