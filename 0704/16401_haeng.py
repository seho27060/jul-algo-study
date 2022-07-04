M,N = map(int, input().split())
snack = list(map(int,input().split()))
snack.sort()
S = 0
E = 1000000000
while S <= E:
    mid = (S+E)//2
    c=0
    if mid == 0:
        break
    for i in snack:
        c += i//mid
    if c>=M:
        S = mid+1
    else:
        E = mid-1
        mid -=1
print(mid)
