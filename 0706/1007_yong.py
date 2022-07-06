#조합을 활용한 벡터풀이 문제
# 요구하는 집단을 구해 문제풀기

import sys
import math
from itertools import combinations

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    X = Y = 0
    for i in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))
        X += x
        Y += y

    minV = 1000000

    for i in combinations(range(n), n // 2):

        x, y = 0, 0
        for j in i:
            x += arr[j][0]
            y += arr[j][1]

        x -= X - x
        y -= Y - y

        V = math.sqrt(x ** 2 + y ** 2)
        if minV > V:
            minV = V
    print(minV)