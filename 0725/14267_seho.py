# 220725 14267 회사 문화 1
# 일방향 그래프? 상사의 칭찬은 내리칭찬이된다.
# n,m < 100,000

import sys

input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))

workers = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    workers[a] += b
# print(workers[1:])
for idx in range(1,n):
    workers[idx+1] += workers[lst[idx]]
print(*workers[1:])