def find(x,I):
    if x == L:
        c = 0
        result = ''
        for i in ST:
            result += i
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                c += 1
        if c >0 and x - c >= 2:
            print(result)
        return
    for i in range(I,C):
        if i in ST: continue
        ST.append(S[i])
        find(x+1,i+1)
        ST.pop()

L,C = map(int,input().split())
S = list(input().split())
S.sort()
ST = []

find(0,0)