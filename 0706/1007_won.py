import sys
input = sys.stdin.readline
# from collections import deque
from itertools import combinations, combinations_with_replacement

T = int(input())

def cal(x, y):
    return (x ** 2 + y ** 2) ** 0.5

for _ in range(T):
    ans = 999999
    N = int(input())
    arr = []
    x_total, y_total = 0, 0
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])
        x_total += a
        y_total += b

    h = int(N / 2)
    arr = list(combinations(arr, h))
    # print(arr)
    h = int(len(arr) / 2)
    for comb in arr[:h]:
        # print(comb)
        x1_total, y1_total = 0, 0
        for x, y in comb:
            x1_total += x
            y1_total += y
        x2_total = x_total - x1_total
        y2_total = y_total - y1_total

        res = cal(x1_total - x2_total, y1_total - y2_total)
        ans = min(ans, res)
    print(ans)

