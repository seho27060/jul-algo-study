import sys
input = sys.stdin.readline
# from collections import deque

# 8, 2
N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

l = 0
r = 100000 * 20 + 1

while l <= r:
    mid = (l + r) // 2
    group = 0
    sumV = 0

    for i in range(N):
        sumV += arr[i]
        if sumV >= mid:
            group += 1
            sumV = 0

    if group == K:
        ans = mid
        l = mid + 1
    elif group > K:
        l = mid + 1
    else:
        r = mid - 1
print(ans)

