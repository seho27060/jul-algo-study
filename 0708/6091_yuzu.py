import collections
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n + 1)]
edges = []

for i in range(1, n):
    lst = list(map(int, input().split()))
    k = i+1
    for l in lst:
        edges.append((l, i, k))
        k += 1
edges.sort()

ans = collections.defaultdict(list)
for edge in edges:
    dist, a, b = edge
    if find(a) != find(b):
        union(a, b)
        ans[a].append(b)
        ans[b].append(a)

for i in range(1, n+1):
    print(len(ans[i]), *sorted(ans[i]))