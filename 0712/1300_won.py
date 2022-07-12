import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
l = 1
r = K
ans = 0
while l <= r:
    mid = (l + r) // 2

    tmp = 0
    for i in range(1, N + 1):
        tmp += min(N, mid // i)

    if tmp == K:
        ans = mid
        r = mid - 1
    elif tmp > K:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)
