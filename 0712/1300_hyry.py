def check(val):
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(val // i, N)
    return cnt >= K


def parametric():
    left, right = 1, 1e10
    ans = 1e10 + 1

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
            ans = min(ans, mid)
        else:
            left = mid + 1

    return int(ans)


N = int(input())
K = int(input())

print(parametric())