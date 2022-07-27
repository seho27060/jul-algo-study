N = int(input())
lst = list(map(int, input().split()))
fac = [0, 1]
for i in range(2, N+1):
    fac.append(fac[i-1] * i)
arr = list(range(1, N+1))
if lst[0] == 1:
    ans = []
    k = lst[1] -1
    for num in range(N-1, 0, -1):
        ans.append(arr[k//fac[num]])
        del arr[k//fac[num]]

        k %= fac[num]
    ans.append(arr[0])
    print(*ans)
else:
    cnt = 0
    lst = lst[1:]
    num = N-1
    for i in range(len(lst)):
        cnt += fac[num]*arr.index(lst[i])
        del arr[arr.index(lst[i])]
        num -= 1
    print(cnt+1)