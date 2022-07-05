T = int(input())
for t in range(T):
    F = int(input())
    N = []
    P = {}
    for _ in range(F):
        a,b = input().split()
        if a in P and b in P:
            if P[a] != P[b]:
                small = min(P[a], P[b])
                big = max(P[a],P[b])
                N[small] = N[P[a]]+N[P[b]]
                for i in P:
                    if P[i] >= big:
                        if P[i] == big:
                            P[i] = small
                        else:
                            P[i] -= 1
                N.pop(big)
                print((N[small]))

            else:
                print(N[P[a]])
        elif a not in P and b not in P:
            N.append(2)
            P[a] = len(N)-1
            P[b] = len(N)-1
            print(2)
        else:
            if a in P:
                N[P[a]] += 1
                P[b] = P[a]
            else:
                N[P[b]] += 1
                P[a] = P[b]
            print(N[P[a]])