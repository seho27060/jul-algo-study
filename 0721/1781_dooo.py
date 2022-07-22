import heapq

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

q = []

for i in arr:
    heapq.heappush(q, i[1])
    if i[0] < len(q):
        heapq.heappop(q)

print(sum(q))