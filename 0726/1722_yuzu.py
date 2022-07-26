dic = {}
def findfac(n):
    global dic
    if n in dic:
        return dic[n]
    elif n <= 1:
        return 1
    else:
        dic[n] = n * findfac(n - 1)
        return dic[n]

n = int(input())
lst = list(map(int, input().split()))

if lst[0] == 1:
    k = lst[1]
    ans = []
    nums = list(range(1, n + 1))
    for i in range(n):
        x = findfac(n - 1 - i)
        w = (k - 1) // x
        ans.append(nums[w])
        nums.remove(nums[w])
        k -= x * (w)
    print(*ans)

else:
    per = lst[1:]
    sortedper = list(sorted(per))
    ans = 1
    for i in range(n):
        w = sortedper.index(per[i])
        sortedper.remove(per[i])
        x = findfac(n - 1 - i)
        ans += x * w
    print(ans)