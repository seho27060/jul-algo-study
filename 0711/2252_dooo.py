from collections import deque

n, m = map(int, input().split())
cnt = [0] * (n+1)
G = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    cnt[b] += 1
q = deque()

for i in range(1 , n+1):
    if cnt[i] == 0:
        q.append(i)
ans = []
while q:
    c = q.popleft()
    ans.append(c)
    for j in G[c]:
        cnt[j] -= 1
        if cnt[j] == 0:
            q.append(j)
print(*ans)