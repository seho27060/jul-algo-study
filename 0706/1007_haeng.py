def find(level, s, e,I):
    global result
    if level == N/2:
        minusX = X - s
        minusY = Y - e
        if result > ((s-minusX)**2+(e-minusY)**2)**0.5:
            result = ((s-minusX)**2+(e-minusY)**2)**0.5
        return

    for i in range(I+1,N):
        if V[i]: continue
        V[i] = 1
        find(level+1,s+P[i][0],e+P[i][1],i)
        V[i] = 0

T = int(input())
for t in range(T):
    N = int(input())
    P = []
    X,Y=0,0
    for _ in range(N):
        a,b = map(int,input().split())
        X += a
        Y += b
        P.append((a,b))

    V = [0]*N
    ST = []
    result = 99999999999999999
    find(0, 0, 0,0)

    print(result)