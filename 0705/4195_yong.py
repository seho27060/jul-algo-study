# Union, find 문제
# 부모로 자기자신을 갖는 원소를 생성
# find를 통해 들어온 원소의 Root노드를 반환
# union을 통해 y가 x의 자식인자가 되도록 만듬

def find(x):
    if x == p_dic[x]:
        return x
    else:
        rootX = find(p_dic[x])
        p_dic[x] = rootX
        return p_dic[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        p_dic[rootY] = rootX
        n_dic[rootX] += n_dic[rootY]


T = int(input())

for tc in range(T):
    F = int(input())
    p_dic = dict()
    n_dic = dict()
    for _ in range(F):
        F1, F2 = map(str, input().split())
        
        if F1 not in p_dic:
            p_dic[F1] = F1
            n_dic[F1] = 1
        if F2 not in p_dic:
            p_dic[F2] = F2
            n_dic[F2] = 1

        union(F1, F2)
        print(n_dic[find(F1)])