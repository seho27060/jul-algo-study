import sys
INF = sys.maxsize

n = int(input())

A = [[0] * (n+1)]
for _ in range(n):
    A.append([0] + list(map(int, input().split())))

DP = [[0] * (n+1)] + [[0] + [INF] * n for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            DP[i][j] = 0

        if -1 < i+1 < n+1:
            if A[i+1][j] < A[i][j]:
                DP[i + 1][j] = min(DP[i][j], DP[i + 1][j])
            else:
                DP[i + 1][j] = min(DP[i+1][j], DP[i][j] + A[i + 1][j] - A[i][j] + 1)

        if -1 < j+1 < n+1:
            if A[i][j+1] < A[i][j]:
                DP[i][j + 1] = min(DP[i][j], DP[i][j + 1])
            else:
                DP[i][j + 1] = min(DP[i][j+1], DP[i][j] + A[i][j + 1] - A[i][j] + 1)

print(DP[-1][-1])
