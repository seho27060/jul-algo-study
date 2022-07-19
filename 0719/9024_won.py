import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
from itertools import combinations

t = int(input())

for _ in range(t):
    n, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    target = 10 ** 8 * 2
    cnt = 0
    for i in range(n):
        l = i + 1
        r = n - 1
        while l <= r:
            mid = (r + l) // 2
            sumV = arr[i] + arr[mid]
            diff = abs(sumV - K)

            if sumV > K:
                r = mid - 1
            else:
                l = mid + 1

            if target > diff:
                target = diff
                cnt = 1
            elif target == diff:
                cnt += 1
    print(cnt)
