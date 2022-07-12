from collections import deque

N,M = map(int,input().split())
key = {i:[] for i in range(1,N+1)}
V = [0]*(N+1)
C = [0]*(N+1)
Q = deque()
for _ in range(M):
    a,b = map(int,input().split())
    key[b].append(a)
    C[a] +=1

for i in range(1,N+1):
    if C[i] == 0:
        Q.append(i)
        V[i] = 1
result = deque()
while Q:
    n = Q.popleft()
    result.appendleft(n)
    for i in key[n]:
        C[i] -= 1
        if C[i] == 0:
            Q.append(i)
            V[i] = 1
print(*result)