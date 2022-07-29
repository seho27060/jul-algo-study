from collections import deque
import sys
input = sys.stdin.readline

def bfs(X):
    visit=[0]*(N+1)
    ST = deque()
    ST.append(s)
    while ST:
        now = ST.popleft()
        if now == e: return 2
        for i in road[now]:
            if visit[i[0]] == 0 and X<=i[1]:
                ST.append(i[0])
                visit[i[0]] = 1


N,M = map(int,input().split())
s,e = map(int,input().split())
road=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    road[a].append((b,c))
    road[b].append((a,c))

max_weight = 1000001
min_weight = 1

while min_weight <= max_weight:
    mid = (max_weight+min_weight)//2
    if bfs(mid):
        min_weight = mid+1
    else:
        max_weight = mid-1

print(min_weight-1)