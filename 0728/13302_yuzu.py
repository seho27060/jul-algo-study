import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
if m == 0:
    lst = []
else:
    lst = list(map(int, input().split()))

dp = [[INF]*106 for _ in range(106)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(40):
        if dp[i][j] == INF:
            continue
        tmp = dp[i][j]
        if i+1 in lst:
            dp[i+1][j] = min(tmp, dp[i+1][j])
        if j >= 3:
            dp[i+1][j-3] = min(tmp, dp[i+1][j-3])
        dp[i+1][j] = min(tmp+10000, dp[i+1][j])
        for p in range(1, 4):
            dp[i+p][j+1] = min(tmp+25000, dp[i+p][j+1])
        for q in range(1, 6):
            dp[i+q][j+2] = min(tmp+37000, dp[i+q][j+2])
print(min(dp[n]))