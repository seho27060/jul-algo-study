import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    answer[u] += v

for i in range(n):
    if lst[i] != -1:
        graph[lst[i]].append(i+1)

def dfs(x):
    for i in graph[x]:
        answer[i] += answer[x]
        dfs(i)

dfs(1)
print(*answer[1:])