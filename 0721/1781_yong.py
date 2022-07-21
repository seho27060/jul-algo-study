# 힙큐를 활용한 우선순위큐 문제
# 데드라인을 기준으로 오름차순 후 최소값을 제거하며 진행한다.

import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    d, r = map(int, input().split())
    arr.append((d, r))

arr.sort()

q = []

for i in arr:
    heapq.heappush(q, i[1])
    if i[0] < len(q):
        heapq.heappop(q)
print(sum(q))