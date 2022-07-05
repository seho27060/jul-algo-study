def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(a, b):
    a = find(p, a)
    b = find(p, b)
    if a != b:
        p[b] = a
        net[a] += net[b]
    print(net[a])


TC = int(input())
for _ in range(TC):
    p = dict()
    net = dict()
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        if a not in p:
            p[a] = a
            net[a] = 1
        if b not in p:
            p[b] = b
            net[b] = 1

        union(a, b)