from collections import deque
import sys
input = sys.stdin.readline

def check(X):
    c=0
    if visit[X]: return 0
    if X%2 ==0: return 0
    for k in range(1,X+1):
        if X%k == 0:
            c +=1
        if c >2:
            return 0
    if c == 2:
        return 1


def change(A,B,C,D,cnt):
    for j in range(0,10):
        num = str(j)+B+C+D
        if num[0] != '0' and check(int(num)):
            ST.append((num,cnt+1))
            visit[int(num)] =1

        num = A + str(j) + C + D
        if check(int(num)):
            ST.append((num, cnt + 1))
            visit[int(num)] = 1

        num = A + B + str(j) + D
        if check(int(num)):
            ST.append((num, cnt + 1))
            visit[int(num)] = 1

        num = A + B + C + str(j)
        if check(int(num)):
            ST.append((num, cnt + 1))
            visit[int(num)] = 1

T = int(input())
for t in range(T):
    S,E = map(str,input().split())

    result = 0
    ST = deque()
    ST.append((S,0))
    visit = { i:0 for i in range(1000,10000)}
    while ST:
        password,cnt = ST.popleft()
        A,B,C,D = password
        if password == E:
            result = 1
            break

        change(A,B,C,D,cnt)

    if result:
        print(cnt)
    else:
        print('Impossible')