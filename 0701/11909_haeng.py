def up(x,y):
    if road[y][x] < road[y-1][x] and dp[y][x] > dp[y-1][x]:
        return dp[y-1][x]
    elif road[y][x] >= road[y-1][x] and dp[y][x] > dp[y-1][x]:
        return dp[y-1][x]+road[y][x]-road[y-1][x]+1

def left(x,y):
    if road[y][x] < road[y][x-1] and dp[y][x] > dp[y][x-1]:
        return dp[y][x-1]
    elif road[y][x] >= road[y][x-1] and dp[y][x] > dp[y][x-1]:
        return dp[y][x-1]+road[y][x]-road[y][x-1]+1

n = int(input())
road = []
for _ in range(n):
    road.append(list(map(int,input().split())))

dp = [[9999999999]*n for _ in range(n)]
dp[0][0]=0

for y in range(n):
    for x in range(n):
        if x==0 and y ==0:continue
        elif x == 0:
            dp[y][x] = up(x,y)
        elif y == 0:
            dp[y][x] = left(x,y)
        else:
            dp[y][x] = min(left(x,y),up(x,y))
print(dp[n-1][n-1])
