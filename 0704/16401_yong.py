# 이분탐색 문제
# 탐색을 진행하며 만들 수 있는 과자의 수가 아이들 수 이상인 경우를 탐색
def binary(val):
    global ans
    cnt = 0
    for i in snack:
        cnt += i//val
    if cnt >= M:
        ans = val
        return True
    else:
        return False

M, N = map(int, input().split())
ans = 0
snack = list(map(int, input().split()))
minL = 1
maxL = 1000000000
while minL <= maxL:
    midL = (minL + maxL) // 2
    if binary(midL):
        minL = midL+1
    else:
        maxL = midL-1
print(ans)