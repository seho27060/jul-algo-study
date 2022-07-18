import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(int(input()))
lst += lst[0:k-1]
max_val = -1

cnt = [0] * (d+1)
ans = 0
for i in range(k):
    if cnt[lst[i]] == 0:
        cnt[lst[i]] += 1
        ans += 1
    else:
        cnt[lst[i]] += 1
for j in range(k, len(lst)):
    if cnt[lst[j-k]] == 1:
        ans -= 1
        cnt[lst[j-k]] -= 1
    else:
        cnt[lst[j-k]] -= 1
    if cnt[lst[j]] == 0:
        cnt[lst[j]] += 1
        ans += 1
    else:
        cnt[lst[j]] += 1
    if cnt[c] == 0:

        if max_val < ans+1:
            max_val = ans+1
    else:
        if max_val < ans:
            max_val = ans
print(max_val)