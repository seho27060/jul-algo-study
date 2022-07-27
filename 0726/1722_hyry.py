def findK():
    global K
    K -= 1
    depth = 0
    res = []

    while depth < N:
        if cnts[depth]:
            res.append(nums.pop(K // cnts[depth]))
            K %= cnts[depth]
        else:
            res.append(nums.pop())
        depth += 1

    return res

def findPerm():
    depth = 0
    res = 1
    while depth < N:
        for idx, num in enumerate(nums):
            if arr[depth] > num:
                res += cnts[depth]
            else:
                nums.pop(idx)
                break
        depth += 1
    return res


N = int(input())
M, *arr = map(int, input().split())

cnts = [1] * N
nums = [i for i in range(1, N + 1)]

for idx in range(1, N - 1):
    cnts[idx + 1] *= (idx + 1) * cnts[idx]

cnts[0] = 0
cnts.reverse()

if M == 1:
    K = arr[0]
    print(*findK())
else:
    print(findPerm())