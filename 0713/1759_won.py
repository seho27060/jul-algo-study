import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = list(input().split())

vowel = ['a', 'e', 'i', 'o', 'u']
# c = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
arr.sort()
# print(arr)

def checkV(strV):
    cnt = 0
    for i in strV:
        if i in vowel:
            cnt += 1
            if cnt >= 1:
                return True
    return False

def checkC(strV):
    cnt = 0
    for i in strV:
        if i not in vowel:
            cnt += 1
            if cnt >= 2:
                return True
    return False

def f(x, res):
    if x == C:
        if len(res) == L and checkV(res) and checkC(res):
            print(res)
        return
    f(x + 1, res + arr[x])
    f(x + 1, res)
    return

f(0, '')
