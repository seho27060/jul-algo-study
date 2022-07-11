N = int(input())
k = int(input())

S, E = 1, k
while S <= E:
    M = (S+E) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(M // i, N)
    if cnt >= k:
        E = M - 1
    else:
        S = M + 1
print(S)
