import sys
input = sys.stdin.readline

n,m = map(int,input().split())
employee = list(map(int,input().split()))
dp = [0]*(n+1)
mentor = { i:[] for i in range(1,n+1)}

for i in range(1,n):
    mentor[employee[i]].append(i+1)

for _ in range(m):
    a,b = map(int,input().split())
    dp[a] += b

ST = [1]
while ST:
    now = ST.pop(0)
    for i in mentor[now]:
        dp[i] += dp[now]
        ST.append(i)

print(*dp[1:])
