import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N, M = map(int, input().split())
s, e = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    h1, h2, k = map(int, input().split())
    G[h1].append([h2, k])
    G[h2].append([h1, k])

def f(cnt):
    qu = deque()
    qu.append(s)
    visited = [0] * (N + 1)
    visited[s] = 1
    while qu:
        cur = qu.popleft()

        if cur == e:
            return 1

        for new, new_cnt in G[cur]:
            if visited[new] == 0 and new_cnt >= cnt:
                qu.append(new)
                visited[new] = 1
    return 0

ans = 0
l = 1
r = 1000000
while l <= r:
    mid = (l + r) // 2
    if f(mid):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)
