t = int(input())

primeNumber = []
arr = [False, False] + [True]*(9999)

for j in range(2, 10000):
    if arr[j] == True:
        primeNumber.append(j)
        for k in range(2*j, 10000, j):
            arr[k] = False

def solve(s):
    q = [(s, 0)]
    visited = [0 for _ in range(10000)]
    visited[s] = 1

    while q:
        x, cnt = q.pop(0)
        if x == e:
            return cnt
        x = str(x)
        for i in range(4):
            for j in range(10):
                num = int(x[:i] + str(j) + x[i+1:])
                if visited[num] == 0 and num in primeNumber and num >= 1000:
                    visited[num] = 1
                    q.append((num, cnt+1))

for _ in range(t):
    s, e = map(int, input().split())
    if solve(s) != None:
        print(solve(s))
    else:
        print("Impossible")