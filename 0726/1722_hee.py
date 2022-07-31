import sys, math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def func1(arr, sum_val, prev_num, n):
    temp = math.factorial(n)
    temp += sum_val

    if num <= temp:
        V[prev_num] = True
        arr.append(prev_num)

        if len(arr) == N:
            global ans
            ans = arr
            return

        for i in range(1, N+1):
            if not V[i]:
                func1(arr, sum_val, i, n-1)
                break

    else:
        for i in range(prev_num + 1, N+1):
            if not V[i]:
                func1(arr, temp, i, n)
                break

def func2(idx, sum_val, prev_num):
    global ans
    if idx == N-1:
        ans += sum_val
        return

    if nums[idx] == prev_num:
        ans += sum_val
        V[prev_num] = True
        for i in range(1, N+1):
            if not V[i]:
                func2(idx+1, 0, i)
                break
    else:
        for i in range(prev_num + 1, N+1):
            if not V[i]:
                func2(idx, sum_val + math.factorial(N-idx-1), i)
                break

if A[0] == 1:
    num = A[1]
    ans = []
    V = [False] * (N + 1)
    func1([], 0, 1, N-1)
    print(*ans)

else:
    nums = A[1:]
    ans = 0
    V = [False] * (N + 1)
    func2(0, 0, 1)
    print(ans+1)