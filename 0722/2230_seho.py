#220722 2230 수 고르기
# n < 100,000
# m <2,000,000,000 20억
# 차이가 m 이상이면서 가장 작은 값 출력.

import sys

input = sys.stdin.readline

n, m = map(int,input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
# print(lst)
start, end = 0, 1
answer = float('inf')
while start < n and end < n:
    output = abs(lst[start] - lst[end])
    # print(start,end, output)
    if output < m:
        end += 1
    else:
        answer = min(answer, output)
        start += 1
print(answer)
