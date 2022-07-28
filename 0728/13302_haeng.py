N,M =map(int,input().split())

Mlist = []
if M>0:
    Mlist = list(map(int,input().split()))

dp=[[9999999999999]*106 for _ in range(106)]
dp[0][0] = 0
for i in range(N+1):
    for j in range(40):
        if dp[i][j] == 9999999999999: continue

        cash = dp[i][j]
        if i+1 in Mlist:
            dp[i+1][j] = min(cash,dp[i+1][j])

        if j>=3:
            dp[i+1][j-3] = min(cash,dp[i+1][j-3])


        dp[i+1][j] = min(cash+10000,dp[i+1][j])
        for k in range(1,4):
            dp[i+k][j+1] = min(cash+25000,dp[i+k][j+1])
        for k in range(1,6):
            dp[i+k][j+2] = min(cash+37000,dp[i+k][j+2])
print(min(dp[N]))