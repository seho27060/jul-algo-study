import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
T = int(input())

def find(x):
    if x == P[x]:
        return x
    else:
        temp = find(P[x])
        P[x] = temp
        return P[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        P[b] = a
        C[a] += C[b]

def create(x):
    if x not in P:
        P[x] = x
        C[x] = 1

for _ in range(T):
    F = int(input())
    P = dict()
    C = dict()
    for _ in range(F):
        A, B = map(str, input().split())
        create(A)
        create(B)
        union(A, B)
        print(C[find(A)])
