import heapq

def find2():
    v = [99999999999]*(N+1)
    v[2] = 0
    ST = []
    dp=[0]* (N+1)
    dp[2] = 1
    heapq.heappush(ST, (0, 2))
    while ST:
        cnt, now = heapq.heappop(ST)
        if cnt > v[now]: continue
        for c, next in road[now]:
            if v[next] > cnt+c:
                v[next] = cnt+c
                heapq.heappush(ST, (cnt+c, next))
            if cnt > v[next]:
                dp[now] += dp[next]

    return dp[1]


N,M = map(int,input().split())
road = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    road[a].append((c,b))
    road[b].append((c,a))

print(find2())

