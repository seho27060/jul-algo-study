TC = int(input())
for _ in range(TC):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    min_val = 2e9
    cnt = 0
    for i in range(n):
        start = i + 1
        end = n-1
        while start <= end:
            mid = (start+end)//2

            if lst[i] + lst[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
            if abs(k - lst[i] - lst[mid]) < min_val:
                min_val = abs(k-lst[i]-lst[mid])
                cnt = 1
            elif abs(k - lst[i] - lst[mid]) == min_val:
                cnt += 1
    print(cnt)