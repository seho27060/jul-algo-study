def nCr(k,r,s):
    if r == 0:
        cnt = 0

        for w in ['a', 'e', 'i', 'o', 'u']:
            if w in comb:
                cnt += 1

        if cnt >= 1 and n-cnt >= 2:

            print(''.join(comb[::-1]))
    else:
        for i in range(s, k-r+1):

            comb[r-1]= lst[i]
            nCr(k, r-1, i +1)
n, m = map(int, input().split())
lst = list(input().split())
lst.sort()
comb = [0] * n
nCr(m, n, 0)
