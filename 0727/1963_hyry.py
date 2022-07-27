import sys
input = sys.stdin.readline


def isPrime(num):
    if num <= 1: return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def bfs():
    Q = [(S, 0)]
    visit[int(S)] = True

    while Q:
        curV, cnt = Q.pop(0)
        if curV == G:
            return cnt

        for pos in range(4):
            for i in range(10):
                if pos == i == 0: continue
                newV = curV[:pos] + str(i) + curV[pos + 1:]
                if not visit[int(newV)]:
                    visit[int(newV)] = True
                    if isPrime(int(newV)):
                        Q.append((newV, cnt + 1))

    return 'Impossible'


T = int(input())
for _ in range(T):
    S, G = input().split()
    visit = [False] * 10000
    print(bfs())