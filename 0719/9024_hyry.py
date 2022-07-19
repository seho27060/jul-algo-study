
import sys
input = sys.stdin.readline
inf = sys.maxsize

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    left, right = 0, N - 1
    minDiff = inf
    cnt = 0

    while left < right:
        sumV = arr[left] + arr[right]
        diff = abs(K - sumV)

        if minDiff > diff:
            minDiff = diff
            cnt = 1
        elif minDiff == diff:
            cnt += 1

        if sumV > K:
            right -= 1
        else:
            left += 1

    print(cnt)