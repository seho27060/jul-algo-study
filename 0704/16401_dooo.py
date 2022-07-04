n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
start = 1
end = lst[-1]
max_val = 0
while start <= end:
    cnt = 0
    middle =(start + end)//2
    for i in range(len(lst)):
        cnt += lst[i] // middle
    if cnt >= n:
        if max_val < middle:
            max_val = middle
        start = middle + 1
    else:
        end = middle - 1
print(max_val)