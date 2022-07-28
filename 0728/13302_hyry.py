N, M = map(int, input().split())

if M: arr = set(map(int, input().split()))
else: arr = set()

memo = [[1e10] * 110 for _ in range(110)]
memo[0][0] = 0

for day in range(N + 1):
    for coupon in range(41):
        tmp = memo[day][coupon]
        if tmp == 1e10: continue
        if day + 1 in arr:
            memo[day + 1][coupon] = min(tmp, memo[day + 1][coupon])
        if coupon >= 3:
            memo[day + 1][coupon - 3] = min(tmp, memo[day + 1][coupon - 3])

        memo[day + 1][coupon] = min(tmp + 10000, memo[day + 1][coupon])
        memo[day + 3][coupon + 1] = min(tmp + 25000, memo[day + 3][coupon + 1])
        memo[day + 5][coupon + 2] = min(tmp + 37000, memo[day + 5][coupon + 2])

print(min(memo[N]))