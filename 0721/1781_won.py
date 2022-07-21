import sys
input = sys.stdin.readline
# from collections import deque
from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import combinations

N = int(input())

arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()

# print(arr)

qu = []

for a, b in arr:
    heappush(qu, b)
    if a < len(qu):
        heappop(qu)

print(sum(qu))
