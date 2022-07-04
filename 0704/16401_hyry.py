'''
parametric search 이용
(binary search의 bisect_left, bisect_right 개념)

자르는 막대 길이를 x라 할 때
x로 자르면 몇 명의 조카에게 나눠 줄 수 있을지 계산 (check)

조카의 수가 지금 제시된 조카 수보다 많거나 같은 경우 True
적은 경우 False

True인 경우 binary search에서 left = mid + 1
False인 경우 binary search에서 right = mid - 1

그런데 막대 길이는 그 중 가장 큰 값이어야 하므로 max(ans, mid)

e.g. 
4 3
10 10 15

막대 길이 1 ~ 5) True...
막대 길이 6 ) 나눠 주기 가능한 조카 수 = 4 True
막대 길이 7 ) 나눠 주기 가능한 조카 수 = 4 True
막대 길이 8 ) 나눠 주기 가능한 조카 수 = 8 False 
막대 길이 9 ~ ) False 
'''


def check(val):
    cnt = 0
    for c in candy:
        cnt += c // val

    return cnt >= M


def parametric():
    # left는 막대 사탕 길이로 가능한 가장 작은 값
    # right는 가장 큰 값
    # ans는 불가능할 때 값
    left, right = 1, 1_000_000_000
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
            ans = max(ans, mid)
        else:
            right = mid - 1

    return ans


M, N = map(int, input().split())
candy = list(map(int, input().split()))

print(parametric())
