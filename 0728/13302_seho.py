# 220728 13302 리조트
# 선희는 여름방학이라 리조트에 놀러가..부럽네..
# n < 100, 여름방학 모든날을 리조트에 놀때 최소비용구하기
# dp? 우선탐색? ㅠㅠ

import sys

input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))
dp = [[float("inf")]*106 for _ in range(106)]
dp[0][0] = 0

for day in range(n+1):
    for coupon in range(40):
        if dp[day][coupon] == float('inf'):
            continue
        result = dp[day][coupon]
        if day + 1 in lst:
            dp[day+1][coupon] = min(result,dp[day+1][coupon])
        if coupon >= 3:
            dp[day+1][coupon-3] = min(result,dp[day+1][coupon-3])

        dp[day+1][coupon] = min(dp[day+1][coupon], result + 10000)
        for nxt in range(1,4):
            dp[day+nxt][coupon+1] = min(dp[day+nxt][coupon+1], result+25000)
        for nxt in range(1,6):
            dp[day+nxt][coupon+2] = min(dp[day+nxt][coupon+2], result+37000)
print(min(dp[n]))