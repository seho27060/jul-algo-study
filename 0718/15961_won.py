import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
from collections import defaultdict

N, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(N)]

arr = arr + arr

dict = defaultdict(int)
dict[c] += 1

l = r = 0
ans = 0

while r < k:
    dict[arr[r]] += 1
    r += 1

while r < len(arr):
    ans = max(ans, len(dict))

    dict[arr[l]] -= 1
    if dict[arr[l]] == 0:
        del dict[arr[l]]

    dict[arr[r]] += 1
    r += 1
    l += 1

print(ans)
