def prime():
    p[0], p[1] = 0, 0
    for i in range(2, 10000):
        if p[i] == 1:
            j = 2
            while i * j < 10000:
                p[i*j] = 0
                j +=1


def bfs(s, t):
    q = []
    q.append(s)
    v = [0] * 10000
    v[s] = 1
    while q:
        c = q.pop(0)
        if c == t:
            return v[c]
        c = str(c)
        for i in range(4):
            for j in range(10):
                nn = int(c[:i] + str(j) + c[i+1:])

                if v[nn] == 0 and p[nn] == 1 and nn >= 1000:
                    v[nn] = v[int(c)] + 1

                    q.append(nn)
    return 'Impossible'
p = [1] * 10000
prime()
TC = int(input())
for _ in range(TC):
    n, m = map(int, input().split())
    ans = bfs(n, m)
    print(ans-1)
