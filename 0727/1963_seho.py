#220727 1963 소수 경로
# 창영이 이친구는 비밀번호를 솟수로 만든다
# 멘독세..
# 네자리 소수 두개를 받고 a => b 로 바꾸는 과정에 몇개나 필요할까
# bfs? (nowNum, Cnt)
import sys
from collections import deque

input = sys.stdin.readline

def isItPrime(num):
    for idx in range(2,int(num**(0.5))+1):
        if num%idx == 0:
            return False
    return True

def bfs():
    global answer, visited, numLst, a, b

    queue = deque([a])
    visited[int("".join(a))] = 0

    while queue:
        now = queue.popleft()
        nowNum = int("".join(now))
        # print(nowNum,visited[nowNum])
        if nowNum == b:
            return
        for idx in range(3,-1,-1):
            for num in numLst:
                nxt = now.copy()
                nxt[idx] = num
                nxtNum = int("".join(nxt))
                if 1000<= nxtNum< 10000 and visited[nxtNum] > visited[nowNum] + 1 and isItPrime(nxtNum):
                    visited[nxtNum] = visited[nowNum] + 1
                    queue.append(nxt)

n = int(input())

for tc in range(n):
    answer = 0
    a, b = input().split()
    a = list(a)
    b = int(b)
    # print(a,b)
    visited = [float('inf')]*(10000)
    numLst = [str(i) for i in range(0,10)]
    bfs()
    # print(b,visited[b])
    if visited[b] >= float('inf'):
        print("Impossible")
    else:
        print(visited[b])