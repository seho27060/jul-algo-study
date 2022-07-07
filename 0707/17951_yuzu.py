n, k = map(int, input().split())
scores = list(map(int, input().split()))

l = 0
r = sum(scores)

def group_div(mid):
    s = 0
    cnt = 0
    for score in scores:
        s += score
        if s > mid:
            cnt += 1
            s = 0
    return cnt

while l<=r:
    mid = (l+r)//2
    cnt = group_div(mid)
    if cnt >= k:
        l = mid + 1
    else:
        r = mid - 1
print(l)