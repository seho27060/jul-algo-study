import sys
input = sys.stdin.readline


class DSU:
    def __init__(self, V):
        self.parent = [i for i in range(V + 1)]
        self.rank = [0 for _ in range(V + 1)]
        self.edge_cnt = 0

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
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

        self.edge_cnt += 1

        return True


def bfs():
    Q = [(1_000_000, S)]
    visit = [False] * (V + 1)
    visit[S] = True

    while Q:
        cost, curV = Q.pop(0)
        if curV == G: return cost

        for neiCost, neiV in adj[curV]:
            if not visit[neiV]:
                Q.append((min(cost, neiCost), neiV))
                visit[neiV] = True

    return 0


V, E = map(int, input().split())
S, G = map(int, input().split())

edges = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    edges.append((-w, v1, v2))

edges.sort()

dsu = DSU(V)

adj = [[] for _ in range(V + 1)]
for w, v1, v2 in edges:
    if dsu.union(v1, v2):
        adj[v1].append((-w, v2))
        adj[v2].append((-w, v1))
        if dsu.edge_cnt == V - 1:
            break

print(bfs())