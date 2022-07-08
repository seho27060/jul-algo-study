import heapq

N = int(input())
road = {i: [] for i in range(1, N + 1)}
for i in range(1, N):
    cost = list(map(int, input().split()))
    t = i + 1
    for j in cost:
        road[i].append((j, i, t))
        road[t].append((j, t, i))
        t += 1

V = [0] * (N+1)
V[N] = 1
V[0] = 1
ST = []
for i in road[N]:
    heapq.heappush(ST, i)

Y = {i: [] for i in range(1, N + 1)}
while V[0] < N:
    A = heapq.heappop(ST)
    if V[A[2]]: continue
    Y[A[1]].append(A[2])
    Y[A[2]].append(A[1])
    V[A[2]] = 1
    V[0] += 1
    if V[0] == N-1:
        for j in range(1,N+1):
            if V[j] == 0:
                A = min(road[j])
                Y[A[1]].append(A[2])
                Y[A[2]].append(A[1])
                break
        break
    for i in road[A[2]]:
        if V[i[2]]: continue
        heapq.heappush(ST, i)

for i in range(1,N+1):
    print(len(Y[i]), *sorted(Y[i]))