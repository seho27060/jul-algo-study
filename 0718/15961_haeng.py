import sys
input = sys.stdin.readline
from collections import defaultdict

N,d,k,c = map(int,input().split())

sushi = []
for _ in range(N):
    sushi.append(int(input()))
for i in range(k):
    sushi.append(sushi[i])

eat = defaultdict(int)

for i in range(k):
    eat[sushi[i]] += 1
eat[c] += 1


cnt = len(eat)
result = cnt

for i in range(k,len(sushi)):
    eat[sushi[i-k]] -= 1
    if eat[sushi[i-k]] == 0:
        cnt -=1

    eat[sushi[i]] += 1
    if eat[sushi[i]] == 1:
        cnt +=1

    result = max(cnt, result)

print(result)