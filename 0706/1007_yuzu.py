import sys
import math

def dfs(k, depth):
    global ans
    if depth == m:
        nx = x
        ny = y
        for re in res:
            rx = lst[re][0]
            ry = lst[re][1]
            nx -= 2*rx
            ny -= 2*ry
        ans = min(ans, math.sqrt(nx**2+ny**2))
        return
    for i in range(k, n):
        res[depth] = i
        dfs(i+1, depth+1)

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    m = n//2
    res = [0] * (m)
    lst = []
    x, y = 0, 0
    ans = sys.maxsize
    for _ in range(n):
        a, b = map(int, input().split())
        lst.append((a, b))
        x += a
        y += b
    dfs(0, 0)
    print(ans)