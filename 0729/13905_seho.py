# 220729 13905 세부
# 노드, 그래프, 비용있음
# 노드 < 100,000, 간선 < 300,000
# 출발에서 도착까지 챙길수있는 골드패패로의 최대갯수
import sys
from heapq import *

input = sys.stdin.readline

def djk():
    global n, m, s, e, islands, visited, answer
    queue = []
    heappush(queue,[-1000000,s])

    while queue:
        cost, now = heappop(queue)
        # print(cost,now)
        if now == e:
            print(-cost)
            return
        if visited[now] < cost:
            continue

        for nxt, nxtLimit in islands[now]:
            nxtCost = max(cost,nxtLimit)
            if visited[nxt] > nxtCost:
                visited[nxt] = nxtCost
                heappush(queue,[nxtCost,nxt])

    print(-visited[e])
    return
n, m = map(int,input().split())
s, e = map(int,input().split())
islands =[[] for _ in range(n+1)]
visited = [0]*(n+1)
answer = 0
for _ in range(m):
    h1, h2, k = map(int,input().split())
    islands[h1].append([h2,-k])
    islands[h2].append([h1,-k])

djk()
# print(-visited[e])
# print(answer)