N,K = map(int,input().split())
score = list(map(int,input().split()))
total = sum(score)
S = 0
E = total
result=0
while S<=E:
    mid = (S+E)//2

    V = [0]*K
    gruop = 0
    for i in score:
        V[gruop] += i
        if gruop<K-1 and V[gruop] >= mid:
            gruop += 1
    if gruop==K-1 and V[gruop] >= mid:
        result = max(result,min(V))
        S = mid + 1
    else:
        E = mid-1
print(result)