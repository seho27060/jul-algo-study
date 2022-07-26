def factorial(N):
    if N == 1:
        return N
    return N*factorial(N-1)

def problem1(X,a,level):
    if X < a:
        ST.append(arr.pop(0))
        if level > 1:
            problem1(X, int(a/(level-1)), level - 1)
    else:
        ST.append(arr.pop(X//a))
        if level > 1:
            problem1(X%a, int(a/(level-1)), level - 1)

def problem2(X,a):
    result = 1
    c = N
    for i in X:

        result += arr.index(i) * a
        arr.remove(i)

        c -= 1
        if c != 0:
            a = int(a/c)
    return result


N = int(input())
A = list(map(int,input().split()))
arr = [i for i in range(1,N+1)]
ST = []

Nf = int(factorial(N)/N)

if A[0] == 1:
    problem1(A[1]-1,Nf,N)
    print(*ST)

else:
    print(problem2(A[1:],Nf))