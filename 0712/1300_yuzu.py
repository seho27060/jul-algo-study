n = int(input())
k = int(input())

l = 0
r = n**2

def count():
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    return cnt

while l <= r:
    mid = (l+r)//2
    cnt = count()
    if cnt >= k:
        r = mid - 1
    else:
        l = mid + 1
print(l)