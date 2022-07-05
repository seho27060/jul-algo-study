import sys
input = sys.stdin.readline


class DSU:
    def __init__(self, V):
        self.nameBook = {}
        self.index = 0
        self.parent = [i for i in range(V)]
        self.rank = [1 for _ in range(V)]

    def mapping(self, name):
        if name not in self.nameBook:
            self.nameBook[name] = self.index
            self.index += 1
        return self.nameBook[name]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot: return self.rank[xRoot]

        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += self.rank[yRoot]
            return self.rank[xRoot]
        elif self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
            self.rank[yRoot] += self.rank[xRoot]
            return self.rank[yRoot]
        else:
            self.parent[xRoot] = yRoot
            self.rank[yRoot] += self.rank[xRoot]
            return self.rank[yRoot]


T = int(input())
for _ in range(T):
    N = int(input())

    dsu = DSU(N * 2)
    for _ in range(N):
        f1, f2 = input().split()
        f1_idx = dsu.mapping(f1)
        f2_idx = dsu.mapping(f2)
        print(dsu.union(f1_idx, f2_idx))