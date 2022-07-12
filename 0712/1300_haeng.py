N = int(input())
k = int(input())

s = 1
e = N**2
while s<=e:
    mid = (s+e)//2
    c = 0
    for i in range(1,N+1):
        c += min(N,mid//i)

    if c <k:
        s = mid + 1
    else:
        e = mid - 1

print(s)