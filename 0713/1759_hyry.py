def comb(depth, start, v_cnt, c_cnt):
    if depth == L:
        if v_cnt and c_cnt >= 2:
            print(''.join(word))
        return

    for idx in range(start + 1, C):
        word[depth] = arr[idx]
        if arr[idx] in vowels:
            comb(depth + 1, idx, v_cnt + 1, c_cnt)
        else:
            comb(depth + 1, idx, v_cnt, c_cnt + 1)


L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
word = [''] * L
vowels = {'a', 'e', 'i', 'o', 'u'}
comb(0, -1, 0, 0)