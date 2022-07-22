# 투포인터를 활용한 탐색문제
# 같은 시작점에서 출발하여 조건에 따라 각 포인터를 이동하여 답을 구한다.


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
left = right = 0
ans = 2000000000
while right < N:
    val = arr[right] - arr[left] 
    if val == M:
        print(M)
        exit()
    if val > M and ans > val:
        ans = val
    if left == right or val < M:
        right += 1
    elif val > M:
        left += 1
print(ans)        
