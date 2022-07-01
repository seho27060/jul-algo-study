n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if x == 0 and y == 0:
            continue
        elif x == 0:
            if arr[x][y] < arr[x][y-1]:
                p1 = dp[x][y-1]
            else:
                p1 = dp[x][y-1] + arr[x][y] - arr[x][y-1] + 1
            dp[x][y] += p1
        elif y == 0:
            if arr[x][y] < arr[x-1][y]:
                p2 = dp[x-1][y]
            else:
                p2 = dp[x-1][y] + arr[x][y] - arr[x-1][y] + 1
            dp[x][y] += p2
        else:
            if arr[x][y] < arr[x][y-1]:
                p1 = dp[x][y-1]
            else:
                p1 = dp[x][y-1] + arr[x][y] - arr[x][y-1] + 1
            if arr[x][y] < arr[x-1][y]:
                p2 = dp[x-1][y]
            else:
                p2 = dp[x-1][y] + arr[x][y] - arr[x-1][y] + 1
            dp[x][y] = min(p1, p2)
print(dp[-1][-1])