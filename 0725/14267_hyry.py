import sys
input = sys.stdin.readline


def bfs():
    Q = [1]
    
    while Q:
        curV = Q.pop(0)

        for neiV in newEmp[curV]:
            Q.append(neiV)
            memo[neiV] += memo[curV] + lob.get(neiV, 0)


N, M = map(int, input().split())
emp = list(map(int, input().split()))

newEmp = [[] for _ in range(N + 1)]
for idx in range(1, N):
    newEmp[emp[idx]].append(idx + 1)

lob = dict()
for _ in range(M):
    i, w = map(int, input().split())
    lob[i] = lob.get(i, 0) + w

memo = [0] * (N + 1)
bfs()

print(*memo[1:])