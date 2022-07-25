import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
G = [[] for _ in range(n + 1)]
# parent = [0] * (n + 1)
ans = [0] * (n + 1)

for i in range(n):
    if arr[i] == -1:
        continue
    G[arr[i]].append(i + 1)
    # parent[i + 1] = arr[i]

for _ in range(m):
    a, b = map(int, input().split())
    ans[a] += b


def f():
    qu = deque()
    qu.append(1)
    while qu:
        cur = qu.popleft()

        if G[cur]:
            for new in G[cur]:
                ans[new] += ans[cur]
                qu.append(new)

f()
print(*ans[1:])
