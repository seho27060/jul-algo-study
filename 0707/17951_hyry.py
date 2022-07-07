def check(val):
    cnt = tmpSum = 0

    for num in arr:
        tmpSum += num
        if tmpSum >= val:
            cnt += 1
            tmpSum = 0

    return cnt >= K


def parametric():
    left, right = 0, 2_000_000
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
            ans = max(ans, mid)
        else:
            right = mid - 1

    return ans


N, K = map(int, input().split())
arr = list(map(int, input().split()))

print(parametric())