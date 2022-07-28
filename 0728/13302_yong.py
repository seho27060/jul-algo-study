# 최소비용을 구하는 DP문제
# 2차원 배열을 생성 후 각 일자별 가격을 비교해 더 저렴한 상황을 적용시켜 나간다

import sys
input = sys.stdin.readline
inf = sys.maxsize
n, m = map(int, input().split())
lst = list(map(int, input().split()))

dp = [[inf]*(100) for _ in range(n+6)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(40):
        if dp[i][j] == inf:
            continue
        val = dp[i][j]
        if i+1 in lst:
            dp[i+1][j] = min(val, dp[i+1][j])
        if j >= 3:
            dp[i+1][j-3] = min(val, dp[i+1][j-3])
        dp[i+1][j] = min(dp[i+1][j], val+10000)
        for k in range(1, 4):
            dp[i+k][j+1] = min(dp[i+k][j+1], val+25000)
        k = 0
        for k in range(1, 6):
            dp[i+k][j+2] = min(dp[i+k][j+2], val+37000)
print(min(dp[n]))
