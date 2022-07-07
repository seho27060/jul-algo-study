# 이분탐색 문제
# 받을 수 있는 점수의 최소값을 갱신하며 그룹을 나눌 때 발생하는 점수의 최소를 구하기

N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
left = 0
right = 10**5 * 20

while left <= right:
    mid = (left + right) // 2
    group = 0
    score = 0
    minV = 10**5 * 20
    for i in arr:
        score += i
        if score >= mid:
            if minV > score:
                minV = score
            group += 1
            score = 0
        
    if group >= K:
        ans = minV
        left = mid+1
    else:
        right = mid-1
print(ans)