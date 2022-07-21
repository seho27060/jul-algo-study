# 220721 1781 컵라면
# n <= 200,000 ㅠㅜ

import sys
from heapq import *

input = sys.stdin.readline

n = int(input())

lst = []
for idx in range(1, n+1):
    d, c = map(int,input().split())
    lst.append([d,c,idx])
lst.sort()
queue = []
for l in lst:
    heappush(queue,l[1])
    if l[0] < len(queue):
        heappop(queue)
print(sum(queue))