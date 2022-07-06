# 시초...
# def selectPair(depth, maxNum, sumX, sumY):
#     global minV
#
#     if depth == endOfDepth:
#         minV = min(minV, (sumX ** 2 + sumY ** 2) ** 0.5)
#         return
#
#     for idx in range(lenOfPair):
#         if not mask[idx] and pair[idx][0] not in visit and pair[idx][1] not in visit:
#             if pair[idx][0] > maxNum:
#
#                 mask[idx] = True
#                 visit.add(pair[idx][0])
#                 visit.add(pair[idx][1])
#
#                 x1, y1 = arr[pair[idx][0]]
#                 x2, y2 = arr[pair[idx][1]]
#
#                 selectPair(depth + 1, pair[idx][0], sumX + x2 - x1, sumY + y2 - y1)
#
#                 mask[idx] = False
#                 visit.remove(pair[idx][0])
#                 visit.remove(pair[idx][1])
#
#
# T = int(input())
# for _ in range(T):
#
#     N = int(input())
#     endOfDepth = N // 2
#
#     arr = []
#     for _ in range(N):
#         x, y = map(int, input().split())
#         arr.append((x, y))
#
#     pair = []
#     for i in range(N):
#         for j in range(N):
#             if i == j: continue
#             pair.append((i, j))
#
#     lenOfPair = len(pair)
#     mask = [False] * lenOfPair
#     visit = set()
#
#     minV = 1e10
#     selectPair(0, -1, 0, 0)
#     print(minV)


def selectPair(depth, minidx):
    global minV

    if depth == endOfDepth:
        tmpX = tmpY = 0
        for i in pos:
            a, b = arr[i]
            tmpX += a
            tmpY += b
        minV = min(minV, ((sumX - tmpX * 2) ** 2 + (sumY - tmpY * 2) ** 2) ** 0.5)
        return

    for idx in range(minidx, N):
        if not visit[idx]:
            visit[idx] = True
            pos[depth] = idx
            selectPair(depth + 1, idx + 1)
            visit[idx] = False


T = int(input())
for _ in range(T):
    N = int(input())
    endOfDepth = N // 2

    arr = []
    sumX = sumY = 0
    for _ in range(N):
        x, y = map(int, input().split())
        arr.append((x, y))
        sumX += x
        sumY += y

    pos = [-1] * endOfDepth
    visit = [False] * N

    minV = 1e10
    selectPair(0, 0)
    print(minV)
