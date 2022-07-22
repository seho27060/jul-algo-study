N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()
ans = 1e10
l, r = 0, 0
while l < N and r < N:
    d = abs(A[l]-A[r])
    if d == M:
        ans = M
        break
    elif d > M:
        ans = min(ans, d)
        l += 1
    else:
        r += 1
print(ans)