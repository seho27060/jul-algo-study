#220714 2176 합리적인 이동경로

import sys
from heapq import *

input = sys.stdin.readline

def djk():
    global n, graphs, dst, dp

    queue = []
    heappush(queue,[0,2])

    while queue:
        cost, now = heappop(queue)
        # print(now,visited)
        if cost > dst[now]:
            continue

        for nxt, nxtCost in graphs[now]:
            if cost + nxtCost < dst[nxt]:
                dst[nxt] = cost + nxtCost
                heappush(queue,[dst[nxt],nxt])
            if  cost > dst[nxt]:
                dp[now] += dp[nxt]
    print(dp[1])

n, m = map(int,input().split())
graphs = [[] for _ in range(n+1)]
dst = [float('inf')]*(n+1)
dp = [0]*(n+1)
dst[2] = 0
dp[2] = 1

for _ in range(m):
    a, b, c = map(int,input().split())
    graphs[a].append([b,c])
    graphs[b].append([a,c])

djk()
# for kk in visited:
#     print(kk)