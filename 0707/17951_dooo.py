n, k = map(int, input().split())

lst = list(map(int, input().split()))
ans = 0
start = 0
end = 10**5 * 20 + 1
while start <= end:
    mid = (start+end)//2
    g = 0
    total = 0
    for i in lst:
        total += i
        if total >= mid:
            g += 1
            total = 0
    if g >= k:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)