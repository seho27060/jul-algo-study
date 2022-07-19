# 포인터와 이분탐색을 활용한 문제
# 양쪽 지점을 시작점으로 잡고 합이 k에 근접한가 판단
# 합한 수가 k와 비교했을 때 크냐, 작냐로 left, right이동을 판단

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    numLst = list(map(int, input().split()))
    numLst.sort()
    cnt = 0
    left = 0
    right = n-1
    maxV = 2*(10**8)
    while left < right:
        val = numLst[right] + numLst[left]
        if maxV > abs(k - val):
            cnt = 1
            maxV = abs(k - val)
        elif maxV == abs(k - val):
            cnt += 1
        if k > val:
            left += 1
        else:
            right -= 1
    print(cnt)