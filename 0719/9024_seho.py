#220719 9024 두 수의 합
# 정수 리스트에서 두개의 정수 합이 k에 가장 가까운 수를 구하라

import sys

input = sys.stdin.readline

tc = int(input())

for tc_num in range(tc):
    n, k = map(int,input().split())
    lst = sorted(list(map(int,input().split())))
    start = 0
    end = n - 1
    numDict = {}
    while start < end:
        numSum = lst[start] + lst[end]
        if numSum in numDict.keys():
            numDict[numSum] += 1
        else:
            numDict[numSum] = 1
        if numSum >= k:
            end -= 1
        else:
            start += 1
    # print(numDict)
    sortNum = sorted(numDict.keys(), key= lambda x:abs(x-k))
    # print(sortNum)
    idx = 0
    answer = 0
    answer += numDict[sortNum[idx]]
    if idx + 1< len(sortNum):
        if abs(k-sortNum[idx]) == abs(k-sortNum[idx+1]):
            answer += numDict[sortNum[idx+1]]
    print(answer)