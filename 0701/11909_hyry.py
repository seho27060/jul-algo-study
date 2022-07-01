N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]
memo = [[0] * N for _ in range(N)]

for row in range(N):
    for col in range(N):
        if row == col == 0: continue
        if row == 0:
            if MAP[row][col - 1] > MAP[row][col]:
                memo[row][col] = memo[row][col - 1]
            else:
                memo[row][col] = memo[row][col - 1] + MAP[row][col] + 1 - MAP[row][col - 1]
        elif col == 0:
            if MAP[row - 1][col] > MAP[row][col]:
                memo[row][col] = memo[row - 1][col]
            else:
                memo[row][col] = memo[row - 1][col] + MAP[row][col] + 1 - MAP[row - 1][col]
        else:
            if MAP[row][col - 1] > MAP[row][col]:
                tmpleft = memo[row][col - 1]
            else:
                tmpleft = memo[row][col - 1] + MAP[row][col] + 1 - MAP[row][col - 1]
            if MAP[row - 1][col] > MAP[row][col]:
                tmpupper = memo[row - 1][col]
            else:
                tmpupper = memo[row - 1][col] + MAP[row][col] + 1 - MAP[row - 1][col]
            memo[row][col] = min(tmpleft, tmpupper)

print(memo[N - 1][N - 1])