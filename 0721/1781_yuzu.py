import heapq
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    deadline, cup_noodle = map(int, input().split())
    lst.append((deadline, cup_noodle))
lst.sort()

q = []
for deadline, cup_noodle in lst:
    heapq.heappush(q, cup_noodle)
    if deadline < len(q):
        heapq.heappop(q)

print(sum(q))