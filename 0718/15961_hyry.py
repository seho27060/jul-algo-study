
import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

cnt = [0] * N
eaten = dict()
for i in range(K):
    eaten[sushi[i]] = eaten.get(sushi[i], 0) + 1

maxV = len(eaten) + (C not in eaten)

for i in range(N):
    eaten[sushi[i % N]] -= 1
    if not eaten[sushi[i % N]]:
        del eaten[sushi[i % N]]
    eaten[sushi[(i + K) % N]] = eaten.get(sushi[(i + K) % N], 0) + 1
    maxV = max(maxV, len(eaten) + (C not in eaten))

print(maxV)