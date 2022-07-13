l, c = map(int, input().split())
s = list(input().split())
s.sort()
lst = [0]*l

def dfs(depth, x):
    if depth == l:
        f = 0
        aeiou = 0
        if lst[l-1] in 'aeiou':
            aeiou += 1
        for i in range(l-1):
            if lst[i] > lst[i+1]:
                f = 1
                break
            if lst[i] in 'aeiou':
                aeiou += 1
        if aeiou > 0 and f == 0 and l-aeiou >= 2:
            print(''.join(lst))
        return
    for i in range(x, c):
        lst[depth] = s[i]
        dfs(depth+1, i+1)
dfs(0, 0)