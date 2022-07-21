import sys
input=sys.stdin.readline
from collections import deque

dx =[-2,-1,1,2,-2,-1,1,2]
dy =[-1,-2,-2,-1,1,2,2,1]

dx2=[1,-1,0,0]
dy2=[0,0,1,-1]

def horse():
    ST = deque()
    ST.append((0,0,0,0))
    visited = [[[0,0]]*W for _ in range(H)]
    visited[0][0] =[1,0]
    
    while ST:
        X,Y,cnt,jump = ST.popleft()
        if X == W-1 and Y==H-1:
            print(cnt)
            return

        for j in range(4):
            X1 = X + dx2[j]
            Y1 = Y + dy2[j]
            if 0 <= X1 < W and 0 <= Y1 < H and road[Y1][X1] != 1:
                if visited[Y1][X1][0] and visited[Y1][X1][1] > jump:
                    ST.append((X1, Y1, cnt + 1, jump))
                    visited[Y1][X1][1] = jump
                elif visited[Y1][X1][0] == 0:
                    ST.append((X1,Y1,cnt+1,jump))
                    visited[Y1][X1] = [1,jump]


        if jump < K:
            for i in range(8):
                X1 = X + dx[i]
                Y1 = Y + dy[i]
                if 0 <= X1 < W and 0 <= Y1 < H and road[Y1][X1] != 1:
                    if visited[Y1][X1][0] and visited[Y1][X1][1] > jump+1:
                        ST.append((X1, Y1, cnt+1, jump+1))
                        visited[Y1][X1][1] = jump+1
                    elif visited[Y1][X1][0] == 0:
                        ST.append((X1, Y1, cnt+1, jump+1))
                        visited[Y1][X1] = [1, jump+1]
    print(-1)


K = int(input())
W,H = map(int,input().split())
road=[]
for _ in range(H):
    road.append(list(map(int,input().split())))
horse()
