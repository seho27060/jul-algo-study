# 220713 1759 암호 만들기
import sys

input = sys.stdin.readline

def backtrack(loc,strLen):
    global l, c, strLst, checkStr, answer

    if strLen == l:
        result = "".join([strLst[idx] for idx in range(c) if visited[idx] == 1])
        cnt = 0
        for idx in checkStr:
            if visited[idx] == 1:
                cnt += 1
        if cnt >= 1 and l - cnt >= 2:
            answer.add(result)
        return
    if loc + 1 < c + 1:
        visited[loc] = 1
        backtrack(loc+1,strLen+1)
        visited[loc] = 0
        backtrack(loc+1,strLen)
        return
l, c = map(int,input().split())
strLst = list(input().split())
checkStr = [idx for idx in range(c) if strLst[idx] in ["a","e","i","o","u"]]
visited = [0]*c
answer = set()
backtrack(0,0)
answer = list(answer)
output = []

for ans in answer:
    output.append("".join(sorted(ans)))
output.sort()
for out in output:
    print(out)