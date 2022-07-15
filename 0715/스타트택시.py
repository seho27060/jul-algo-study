dx=[1,-1,0,0]
dy=[0,0,1,-1]

def find(nowTaxi):        #가까운 사람찾기
    global target,oil
    ST = [nowTaxi+[0]]
    short_dist = N**2
    short = []
    visited =[[0]*N for _ in range(N)]
    visited[nowTaxi[0]][nowTaxi[1]]=1
    while ST:
        nowy,nowx,cnt = ST.pop(0)

        if (nowy,nowx) in people and cnt <= short_dist:
            short.append([nowy,nowx])
            short_dist = cnt
        for i in range(4):
            Y = nowy + dy[i]
            X = nowx + dx[i]
            if 0<=Y<N and 0<=X<N and road[Y][X] != 1 and cnt+1<=short_dist and visited[Y][X] ==0:
                ST.append((Y,X,cnt+1))
                visited[Y][X] =1


    oil -= short_dist
    if oil <=0:
        print(-1)
        exit()

    if len(short) == 1:
        target = short[0]
    elif len(short) >= 2:
        target = min(short)
    else:
        print(-1)
        exit()

def go(nowPerson):                  #목적지찾기
    global taxi,oil,target

    goal = people[(nowPerson[0],nowPerson[1])]
    ST = [nowPerson+[0]]
    visited = [[0] * N for _ in range(N)]
    visited[nowPerson[0]][nowPerson[1]] = 1
    while ST:
        nowy,nowx,cnt = ST.pop(0)

        if (nowy,nowx) == goal:
            taxi = [nowy,nowx]
            target = 0
            people.pop((nowPerson[0],nowPerson[1]))
            if oil < cnt:
                print(-1)
                exit()
            else:
                oil += cnt
            break

        for i in range(4):
            Y = nowy + dy[i]
            X = nowx + dx[i]
            if 0<=Y<N and 0<=X<N and road[Y][X] != 1 and visited[Y][X] ==0:
                ST.append((Y,X,cnt+1))
                visited[Y][X] =1
    if target:
        print(-1)
        exit()



N,M,oil = map(int,input().split())
road = []
for _ in range(N):
    road.append(list(map(int,input().split())))

taxi = list(map(int,input().split()))
taxi[0] -= 1
taxi[1] -= 1


people = {}
for _ in range(M):
    a,b,c,d = map(int,input().split())
    people[(a-1,b-1)] = (c-1,d-1)

target = 0   #사람이 택시에 타있는경우 target에 people정보를 남김
while people:
    if target:              #사람이 타있을경우는 목적지찾기
        go(target)
    else:                   #사람이 안타있으면 가까운사람찾기
        find(taxi)

print(oil)