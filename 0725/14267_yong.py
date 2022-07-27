# 그래프를 활용한 탐색 문제
# 상사와 부하 직원의 연결 관계를 저장
# 칭찬을 기록한 후 사장부터 시작해 부하직원들에게 계속 칭찬을 펼침

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
con = [[] for _ in range(n+1)]
worker = list(map(int, input().split()))
ans = [0] * (n+1)
superior = [0] * (n+1)
for i in range(1, n):
    con[worker[i]].append(i+1)
    superior[i+1] = worker[i]

q = deque([1])

for i in range(m):
    i, w = map(int, input().split())
    ans[i] += w


while q:
    val = q.popleft()
    for i in con[val]:
        ans[i] += ans[val]
        q.append(i)
print(*ans[1:])