# 220718 15961 회전 초밥
# 벨트위에 같은 초밥 두개 이상 가능
# 1. 한 위치에서 k개의 연속한 초밥
# 2. 1.에 참여할 경우 쿠폰으로 초밥 무료제공/ 벨트에 없으면 무료제공
# 이렇게하는데 가장 많은 가짓수의 초밥을 먹는 경우 출력
# 접시갯수, 초밥 가짓수, 연속초밥, 쿠폰 번호
# 비트마스킹?
# <= 3,000,000 <= 3000 <= 3000 <= d <= 3000
import sys
from collections import deque

input = sys.stdin.readline

n, d, k, c = map(int,input().split())
sushis = [int(input()) for _ in range(n)]

sushis.extend((sushis[:k-1]))

eatSushi = deque()
sushiMenu = [0]*(d+1)
sushiLen = 0
maxLen = 0

for idx, sushi in enumerate(sushis):
    eatSushi.append(sushi)
    # print(idx,sushi)
    sushiMenu[sushi] += 1
    if sushiMenu[sushi] == 1:
        sushiLen += 1

    if idx < k-1:
        continue

    if sushiMenu[c] == 0:
        maxLen = max(maxLen, sushiLen + 1)
    else:
        maxLen = max(maxLen,sushiLen)
    goneSushi = eatSushi.popleft()
    sushiMenu[goneSushi] -= 1
    if sushiMenu[goneSushi] == 0:
        sushiLen -= 1
print(maxLen)
