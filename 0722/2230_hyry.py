import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
ans = sys.maxsize

i, j = 0, 1
while i <= j < N:
    diff = nums[j] - nums[i]

    if diff >= M:
        ans = min(ans, diff)
        i += 1
    else:
        j += 1

print(ans)