# 정렬 후 단어를 조합하는 bf알고리즘
# 백트래킹을 통해 조건에 맞게 리턴문을 작성

def check(word, idx, vowel, con):
    if len(word) == L:
        if vowel >= 1 and con >= 2:
            print(word)
            return
    for i in range(idx, C):
        if W[i] in vo:
            check(word+W[i], i+1, vowel+1, con)
        else:
            check(word+W[i], i+1, vowel, con+1)


L, C = map(int, input().split())
W = list(map(str, input().split()))
W.sort()

vo = ['a', 'e', 'i', 'o', 'u']
for i in range(C-L+1):
    if W[i] in vo:
        check(W[i], i+1, 1, 0)
    else:
        check(W[i], i+1, 0, 1)