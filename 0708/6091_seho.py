#220708 6091 핑크 플로이드
# n개의 정점으로 이루어진 트리
# n = 1024/ n*n = 1000*1000 = 1,000,000
import sys
from heapq import *

def find(node):
    global parent
    if parent[node] == node:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]

def union(start, end):
    global parent
    pS, pE = find(start), find(end)
    if pS == pE:
        return False
    else:
        parent[pE] = pS
        return True

input = sys.stdin.readline()
n = int(input())
answer = [[] for _ in range(n)]
parent = [i for i in range(n+1)]
lines = []

for start in range(n-1):
    getLines = list(map(int,input().split()))
    for end in range(len(getLines)):
        heappush(lines,[getLines[end],start+1,start+end+2])

# print(answer)
while lines:
    cost, s, e = heappop(lines)
    if union(s,e):
        answer[s-1].append(e)
        answer[e-1].append(s)

for result in answer:
    print(len(result), *sorted(result))