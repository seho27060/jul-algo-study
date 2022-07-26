import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


N = int(input())
arr = list(map(int, input().split()))
K = -1
fact = [0, 1, 2, 6, 24, 120]
for i in range(6, 21):
    fact.append(i * fact[i - 1])

n = N
if arr[0] == 1:
    candi = [i for i in range(1, N + 1)]
    K = arr[1] - 1
    res = []
    for _ in range(N - 1):
        tmp = K // fact[n - 1]
        res.append(candi[tmp])
        del candi[tmp]
        K %= fact[n - 1]
        n -= 1
    res.append(candi[0])
    print(*res)
else:
    ans = 1
    target = arr[1:]
    for i in range(N):
        cnt = 0
        for k in range(i, N):
            if i == k:
                continue
            if target[i] > target[k]:
                cnt += 1
        for _ in range(cnt):
            ans += fact[n - 1]
        n -= 1
    print(ans)
