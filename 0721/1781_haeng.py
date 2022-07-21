import sys
input = sys.stdin.readline
import heapq

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))
lst.sort()
day = N
result = 0

cup = []
while day>0:
    while lst and lst[-1][0] >= day:
        a,b = lst.pop()
        heapq.heappush(cup,-b)

    if cup:
        A = heapq.heappop(cup)
        result += -A
    day -= 1
print(result)