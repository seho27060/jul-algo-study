import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    max_size = sys.maxsize
    for i in range(n):
        L = i + 1
        R = n - 1

        while L <= R:
            M = (R + L) // 2
            temp = A[i] + A[M]

            if (temp > K):
                R = M - 1
            else:
                L = M + 1

            if (abs(K - temp) < max_size):
                cnt = 1
                max_size = abs(K - temp)
            elif (abs(K - temp) == max_size):
                cnt += 1
    print(cnt)



