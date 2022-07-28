import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
INF = 99999999999
dp = [[INF] * 106 for _ in range(106)]
dp[0][0] = 0

for i in range(N + 1):
    for k in range(40):
        if dp[i][k] == INF:
            continue
        tmp = dp[i][k]

        if i + 1 in arr:
            dp[i + 1][k] = min(dp[i + 1][k], tmp)
        if k >= 3:
            dp[i + 1][k - 3] = min(dp[i + 1][k - 3], tmp)

        dp[i + 1][k] = min(dp[i + 1][k], tmp + 10000)
        dp[i + 3][k + 1] = min(dp[i + 3][k + 1], tmp + 25000)
        dp[i + 5][k + 2] = min(dp[i + 5][k + 2], tmp + 37000)
print(min(dp[N]))
