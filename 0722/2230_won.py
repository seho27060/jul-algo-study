import sys
input = sys.stdin.readline
# from collections import deque
from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import combinations

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

l = 0
r = 1
ans = 2000000000
while l < N and r < N:
    diff = arr[r] - arr[l]
    if diff == M:
        ans = M
        break
    if diff < M:
        r += 1
    if diff > M:
        ans = min(ans, diff)
        l += 1
print(ans)
