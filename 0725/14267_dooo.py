def bfs(sx):
    q = []
    q.append(sx)

    while q:
        cx = q.pop(0)

        for j in lst[cx]:
            cnt[j] += cnt[cx]
            q.append(j)



n, m = map(int, input().split())
boss = list(map(int, input().split()))
lst = [[] for _ in range(n+1)]
for i in range(n):
    if boss[i] == -1:
        continue
    lst[boss[i]].append(i+1)
p = []
cnt = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] += b

bfs(1)
print(*cnt[1:])