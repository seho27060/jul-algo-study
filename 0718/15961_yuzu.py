import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))
sushi.extend(sushi)

l, r = 0, 0
dic = defaultdict(int)
dic[c] += 1

while r < k:
    dic[sushi[r]] += 1
    r += 1

ans = 0
while r < len(sushi):
    ans = max(ans, len(dic))
    dic[sushi[l]] -= 1
    if dic[sushi[l]] == 0:
        del dic[sushi[l]]
    dic[sushi[r]] += 1
    l += 1
    r += 1

print(ans)