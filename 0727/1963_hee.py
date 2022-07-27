from heapq import *
max_size = 10000
def eratos():
    eratos_list[0] = eratos_list[1] = False
    rt = int(max_size ** 0.5)

    for i in range(2, rt + 1):
        if eratos_list[i] == True:
            for j in range(2 * i, max_size + 1, i):
                eratos_list[j] = False

def func(A, B):
    V = [False] * max_size
    V[A] = True
    Q = [(0, A)]

    while Q:
        cnt, num = heappop(Q)

        if num == B:
            return cnt

        num_list = list(str(num))
        num_list = [int(i) for i in num_list]

        for i in range(4):
            temp = num_list[i]
            for j in range(10):
                num_list[i] = j
                new_num = 1000 * num_list[0] + 100 * num_list[1] + 10 * num_list[2] + num_list[3]
                if 1000 <= new_num and not V[new_num] and eratos_list[new_num]:
                    V[new_num] = True
                    heappush(Q, (cnt+1, new_num))
            num_list[i] = temp
    return 'Impossible'
eratos_list = [True] * (max_size + 1)
eratos()
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(func(A, B))
