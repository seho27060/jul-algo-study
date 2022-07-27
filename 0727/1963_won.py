import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def f(s):
    qu = deque()
    visited = [0 for _ in range(10000)]
    qu.append([s, 0])
    visited[s] = 1
    while qu:
        cur, cnt = qu.popleft()

        if cur == e:
            return cnt

        curStrV = str(cur)

        for i in range(4):
            for k in range(10):
                new = int(curStrV[:i] + str(k) + curStrV[i + 1:])

                if visited[new] == 0 and p[new] == 1 and new >= 1000:
                    qu.append([new, cnt + 1])
                    visited[new] = 1
    return 'Impossible'


T = int(input())
p = [0] * 10000
for i in range(10000):
    if isPrime(i):
        p[i] = 1

for _ in range(T):
    s, e = map(int, input().split())
    ans = f(s)
    print(ans)
