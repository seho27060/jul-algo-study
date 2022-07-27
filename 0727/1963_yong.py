# 에라스토의 체를 활용해 소수를 판단
# 각 자리의 숫자를 바꿔가며 소수인지 판단 후 조건에 맞다면 큐에 저장
# bfs로 진행

from collections import deque
import sys
input = sys.stdin.readline
prm = [1] * 10000
for i in range(2, 10000):
    if prm[i]:
        val = 2*i
        while val < 10000:
            prm[val] = 0
            val += i
# print(prm)
T = int(input())

for tc in range(T):
    ans = -1
    visited = [0] * 10000
    a, b = map(int, input().split())
    q = deque()
    q.append(a)
    visited[a] = 1
    while q:
        val = q.popleft()
        valStr = str(val)
        if val == b:
            ans = visited[val]
            break 
        for i in range(4):
            for j in range(10):
                num = int(valStr[:i] + str(j) + valStr[i+1:])
                if not visited[num] and prm[num] and num >= 1000:
                    visited[num] = visited[val] + 1
                    q.append(num)
    if not visited[b]:
        print("Impossible")
    else:
        print(visited[b]-1)