# 슬라이딩 윈도우를 딕셔너리를 통해 구현
# 추가할 포인터와 삭제할 포인터를 나눠 반복되는 동안 딕셔너리가 지속적으로 갱신되도록 설계

import sys
input = sys.stdin.readline
from collections import defaultdict

N, d, k, c = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst += lst
dic = defaultdict(int)
left = right = ans = 0

for i in range(k):
    dic[lst[i]] += 1
    right += 1

while right < N+k-1:
    if c in dic.keys():
        ans = max(ans, len(dic))
    else:
        ans = max(ans, len(dic)+1)
    dic[lst[left]] -= 1
    if dic[lst[left]] == 0:
        del dic[lst[left]]
    dic[lst[right]] += 1
    left += 1
    right += 1
print(ans)