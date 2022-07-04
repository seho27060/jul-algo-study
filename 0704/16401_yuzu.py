import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

def snack_cut(mid):
    cnt = 0
    for snack in snacks:
        if snack >= mid:
            cnt += (snack//mid)
    return cnt

l = 0
r = max(snacks)
while l <= r:
    mid = (l+r)//2
    if mid == 0:
        r = 0
        break
    cnt = snack_cut(mid)
    if cnt >= m:
        l = mid + 1
    else:
        r = mid - 1

print(r)