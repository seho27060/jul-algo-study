import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = 0
    min = 1e9
    l, r = 0, n-1
    while l < r:
        c = lst[l] + lst[r]
        if c == k:
            l += 1
            r -= 1
        elif k < c:
            r -= 1
        else:
            l += 1

        if abs(c-k) < min:
            min = abs(c-k)
            ans = 1
        elif abs(c-k) == min:
            ans += 1
    print(ans)