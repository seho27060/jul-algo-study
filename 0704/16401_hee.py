import sys
input = sys.stdin.readline

M, N = map(int, input().split())
L = list(map(int, input().split()))

def binary(S, E):
    while S <= E:
        cnt = 0
        mid = (S + E) // 2

        if mid == 0:
            return 0

        for i in L:
            if mid <= i:
                cnt += i // mid

            if M <= cnt:
                S = mid + 1
                break
        else:
            E = mid - 1
    return E

S, E = 0, max(L)
ans = binary(S, E)
print(max(1, ans)) if M <= N else print(ans)
