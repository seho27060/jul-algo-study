L, C = map(int, input().split())
T = sorted(list(input().split()))
A = ['a', 'e', 'i', 'o', 'u']

def func(idx, total, cnt_A, txt):
    if total == L and 1 <= cnt_A and 2 <= total - cnt_A:
        print(txt)

    for i in range(idx, C):
        if T[i] in A:
            func(i+1, total+1, cnt_A+1, txt+T[i])
        else:
            func(i+1, total+1, cnt_A, txt+T[i])

func(0, 0, 0, '')