# 크루스칼을 활용한 인접리스트 구하기
# 부모노드를 탐색하며 연결된 노드들의 관계를 구하여 푸는 문제

def find(val):
    if node[val] != val:
        node[val] = find(node[val])
    return node[val]

def union(val1, val2):
    a = find(val1)
    b = find(val2)

    if a == b:
        return False
    else:
        node[a] = b
        return True

N = int(input())
node = [i for i in range(N+1)]
G = []
result = []
for i in range(N-1):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        G.append((arr[j], i+1, i+j+2))

ans = [[] for _ in range(N+1)]
G.sort()

for v, s, e in G:
    if union(s, e):
        ans[s].append(e)
        ans[e].append(s)

for i in ans[1:]:
    print(len(i), *(sorted(i)), sep=' ')