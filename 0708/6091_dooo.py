import heapq
def find(p, x):
    if p[x] != x:
        return find(p, p[x])
    return x

def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n = int(input())

p = [i for i in range(n+1)]
es = []
for i in range(n-1):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        es.append((lst[j], i+1, i+j+2))
es.sort()

ans = [[] for _ in range(n+1)]
for e in es:

    c, a, b = e

    if find(p,a) != find(p,b):
        union(p, a, b)
        ans[a].append(b)
        ans[b].append(a)

for k in range(1, n+1):
    print(len(ans[k]), *sorted(ans[k]))
