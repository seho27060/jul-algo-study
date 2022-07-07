#220707 17951 흩날리는 시험지 속에서 내 평점이 느껴진거야

import sys

input = sys.stdin.readline

n, k = map(int,input().split())
lst = list(map(int,input().split()))
answer = 0

start = 0
end = sum(lst) + 1

while start <= end:
    mid = (start + end)//2
    groupCnt = 0
    score = 0

    for l in lst:
        score += l
        if score >= mid:
            groupCnt += 1
            score = 0

    if groupCnt < k:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)