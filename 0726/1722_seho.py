# 220726 1722 순열의 순서
# n < 20, k < n!
# 1이면 정렬된 순열에서 k번째 순열 출력
# 2이면 주어진 순열이 몇번째 순열인지 출력

import sys
input = sys.stdin.readline

def getFacto(n):
    answer = 1
    for idx in range(1,n):
        answer = answer*idx
    return answer

def findFacto(n):
    global numLst, answer
    cnt = 0
    facto = getFacto(len(numLst))
    nxtN = n
    while nxtN > facto:
        nxtN -= facto
        cnt += 1
    # print(cnt,numLst,answer)
    if numLst:
        nxtAns = numLst.pop(cnt)
        answer.append(nxtAns)
        findFacto(nxtN)
    else:
        return

def findOrder(getLst):
    global answer, numLst
    findIdx = -1
    if len(numLst) == 1:
        answer += 1
        return
    for idx in range(len(numLst)):
        if getLst[0] == numLst[idx]:
            findIdx = idx
            break
    # print(answer, getFacto(len(numLst)),findIdx,getLst,numLst)
    numLst.pop(findIdx)
    answer += getFacto(len(numLst)+1)*(findIdx)
    findOrder(getLst[1:])
n = int(input())
lst = list(map(int,input().split()))

order = lst[0]
lst = lst[1:]
numLst = [i for i in range(1,n+1)]
# print(order,lst,numLst)
if order == 1:
    answer = []
    findFacto(lst[0])
    print(*answer)
elif order == 2:
    answer = 0
    findOrder(lst)
    print(answer)