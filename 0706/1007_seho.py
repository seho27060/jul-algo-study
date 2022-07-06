# 220706 1007 벡터매칭
# 20개의 좌표 주어짐
# 모든 벡터매칭에서 벡터의 합의 길이가 최소가 되는 값 출력
# 브루트포스인데.. 효율적 브루트포스?

import sys
input = sys.stdin.readline

def calcDst(x,y):
    return (x**2+y**2)**(0.5)

def backtrack(cnt):
    global n, lst, calc, answer
    if sum(calc) == n//2:
        calcX, calcY = 0, 0
        for calcIdx in range(n):
            if calc[calcIdx]:
                calcX -= lst[calcIdx][0]
                calcY -= lst[calcIdx][1]
            else:
                calcX += lst[calcIdx][0]
                calcY += lst[calcIdx][1]
        answer = min(answer, calcDst(calcX,calcY))
    elif cnt < n:
        calc[cnt] = 1
        backtrack(cnt+1)
        calc[cnt] = 0
        backtrack(cnt+1)

tc_num = int(input())

for tc in range(tc_num):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]

    calc = [0]*(n)
    answer = float('inf')
    backtrack(0)
    print(answer)