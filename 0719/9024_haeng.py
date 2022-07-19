import sys
input = sys.stdin.readline
T= int(input())
for t in range(T):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))

    lst.sort()

    result=9999999999999999
    cnt = 0

    left = 0
    right = N-1
    while left<right:
        A = lst[left] + lst[right]
        B = abs(K-A)
        if result > B:
            result = B
            cnt = 1
        elif result == B:
            cnt +=1

        if A > K:
            right -=1
        else:
            left += 1

    print(cnt)
