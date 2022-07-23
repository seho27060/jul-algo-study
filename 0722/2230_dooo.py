n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
min_val = 1123456787543
start = 0
end = 0
flag = 1
while start < n and end < n:
    if lst[end] - lst[start] < m:
        end+= 1
    elif lst[end] - lst[start] == m:
        min_val = m
        break
    else:
        min_val = min(min_val, lst[end] - lst[start])
        start += 1

print(min_val)