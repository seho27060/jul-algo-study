import sys
input = sys.stdin.readline
# from collections import deque

M, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
def check(target):
    cnt = 0
    for i in arr:
        if target <= i:
            cnt += i // target
    return cnt

l = 1
r = arr[-1]
while l <= r:
    mid = (l + r) // 2
    tmp = check(mid)
    if tmp >= M:
        l = mid + 1
    else:
        r = mid - 1

print(r)
