import heapq, sys

def dijk(start):
    q = []
    d[start] = 0
    heapq.heappush(q, (0,start))
    dp[start] = 1
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for j in G[now]:
            cost = dist + j[1]
            if d[j[0]] > cost:
                d[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

            if dist > d[j[0]]:
                dp[now] += dp[j[0]]


n, m = map(int, input().split())
inf = sys.maxsize
G = [[] for _ in range(n+1)]
d = [inf] * (n+1)
dp = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
dijk(2)

print(dp[1])