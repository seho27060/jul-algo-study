# 연결된 리스트를 저장할 그래프와 차수를 저장할 리스트를 생성
# 순서에 맞게 그래프에 저장 후 차수가 0이된 학생을 정답 리스트에 추가
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
# 진입 차수를 저장할 리스트
D = [0 for _ in range(n+1)]
q = deque()
ans = []

for i in range(m):
    f, b = map(int, input().split())
    G[f].append(b)
    D[b] += 1

for i in range(1, n+1):
    if D[i] == 0:
        q.append(i)
    
while q:
    val = q.popleft()
    ans.append(val)
    for i in G[val]:
        D[i] -= 1
        if D[i] == 0:
            q.append(i)

print(*ans) 