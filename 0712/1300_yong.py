# 찾는 값을 열 번호로 나눴을 때 생기는 몫이 구하려는 개수
# 이분탐색을 활용해 풀이

N = int(input())
k = int(input())
s = 1
e = N*N
ans = 1
while s <= e:
    mid = (s+e)//2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt >= k:
        ans = mid
        e = mid-1
    else:
        s = mid+1
print(ans)