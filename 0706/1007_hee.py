import sys
from itertools import combinations
input = sys.stdin.readline
INF = sys.maxsize

T = int(input())
for _ in range(T):
    N = int(input())
    G = []
    temp = [0, 0]

    for _ in range(N):
        A, B = map(int, input().split())
        G.append((A, B))
        temp[0] += A
        temp[1] += B

    ans = INF

    for i in combinations(G, N//2):
        temp_x, temp_y = 0, 0

        for j in i:
            temp_x += j[0]
            temp_y += j[1]

        x, y = temp[0] - 2 * temp_x, temp[1] - 2 * temp_y
        ans = min((x ** 2 + y ** 2) ** 0.5, ans)

    print(ans)


