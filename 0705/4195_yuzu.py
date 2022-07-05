def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return find(parent[x])

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        ans[a] += ans[b]
    return ans[a]

t = int(input())
for _ in range(t):
    f = int(input())
    parent = {}
    ans = {}
    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            ans[a] = 1
        if b not in parent:
            parent[b] = b
            ans[b] = 1
        print(union(a, b))