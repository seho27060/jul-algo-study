import sys
input = sys.stdin.readline


class DSU:
    def __init__(self, V):
        self.parent = [i for i in range(V + 1)]
        self.rank = [0 for _ in range(V + 1)]
        self.edge_cnt = 0
        self.adjList = [[] for _ in range(V + 1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot: return False

        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot

        elif self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot

        else:
            self.parent[xRoot] = yRoot
            self.rank[yRoot] += 1

        self.edge_cnt += 1
        self.adjList[x].append(y)
        self.adjList[y].append(x)

        return True


N = int(input())

edges = []
for v1 in range(1, N):
    weights = map(int, input().split())
    for v2, w in enumerate(weights):
        edges.append((w, v1, v2 + v1 + 1))

edges.sort()

dsu = DSU(N)

for w, v1, v2 in edges:
    if dsu.union(v1, v2):
        if dsu.edge_cnt == N - 1:
            break

for idx in range(1, N + 1):
    dsu.adjList[idx].sort()
    print(len(dsu.adjList[idx]), *dsu.adjList[idx])