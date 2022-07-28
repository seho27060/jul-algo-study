import sys
INF = sys.maxsize
N, M = map(int, input().split())
if M == 0:
    A = []
else:
    A = list(map(int, input().split()))

max_size = (N // 5) * 2 + (N % 5) // 3 + 1
DP = [[INF] * (max_size + 2) for _ in range(N + 6)]
DP[0][0] = 0

for i in range(1, N+1):
    for j in range(max_size):
        if DP[i-1][j] == INF:
            continue

        if i in A:
            DP[i][j] = DP[i-1][j]

        if j >= 3:
            DP[i][j-3] = min(DP[i-1][j], DP[i][j-3])

        DP[i][j] = min(DP[i-1][j] + 10_000, DP[i][j])
        DP[i + 2][j + 1] = min(DP[i - 1][j] + 25_000, DP[i + 2][j + 1])
        DP[i + 4][j + 2] = min(DP[i - 1][j] + 37_000, DP[i + 4][j + 2])
print(min(DP[N]))