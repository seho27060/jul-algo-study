from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())

food = []
for idx in range(N):
    a, b = map(int, input().split())
    food.append((a, b))

food.sort()
Q = []
for i in range(N):
    deadline, ramyeon = food[i]
    heappush(Q, ramyeon)

    while len(Q) > deadline:
        heappop(Q)

print(sum(Q))
