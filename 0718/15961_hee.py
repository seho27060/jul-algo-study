import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
L = [int(input()) for _ in range(N)]
L.extend(L)

V = [0] * (d+1)
V[c] += 1
ans, cnt = 0, 1
for i in range(k):
    if not V[L[i]]:
        cnt += 1
    V[L[i]] += 1

for i in range(k, len(L)):
    ans = max(ans, cnt)
    if L[i-k] == L[i]:
        continue

    V[L[i-k]] -= 1
    if not V[L[i-k]]:
        cnt -= 1

    if not V[L[i]]:
        cnt += 1
    V[L[i]] += 1

print(max(ans, cnt))