N, K = map(int, input().split())
X = list(map(int, input().split()))

S, E = 0, 20 * N
while S <= E:
    M = (S + E) // 2
    cnt, k = 0, 0
    for i in X:
        cnt += i

        if M <= cnt:
            cnt = 0
            k += 1

    if K <= k:
        S = M+1
    else:
        E = M-1
print(E)
