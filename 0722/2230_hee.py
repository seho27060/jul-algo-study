import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()

L, R, ans = 0, 1, INF
while R < N:
    temp = A[R] - A[L]
    if temp < M:
        R += 1
    else:
        L += 1
        ans = min(ans, temp)
print(ans)
