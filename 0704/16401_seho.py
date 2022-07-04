#220704 16401 과자 나눠주기
# m, n 은 1,000,000
# 과자 길이는 10억
# 과자 리스트중 나눠줄 수 있는 과자의 최대 길이 출력.
import sys

input = sys.stdin.readline

m, n = map(int,input().split())

lst = list(map(int,input().split()))

start = 0
end = 1000000000

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        end = 0
        break

    result = 0
    for snack in lst:
        result += snack//mid

    if result >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)