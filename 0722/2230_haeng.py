N,M = map(int,input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

left = 0
right = 1
result = 2000000001
while right<N and left <N:
    A = lst[right] - lst[left]
    if A >= M:
        if A < result:
            result=A
        left += 1

    else:
        right += 1
print(result)
