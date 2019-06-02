
# 05_FenceRepair をヒープで解く
import heapq

# 板の集合から最も短い2つの板を取り出し、長さが2つの板の長さの和になるような板を板の集合に追加

N = int(input())
L = list(map(int,input().split()))

ans = 0

que = []

for i in range(len(L)):
    heapq.heappush(que,L[i])

while (len(que) > 1):
    #1番短い板、次に短い板を
    l1 = heapq.heappop(que)
    l2 = heapq.heappop(que)

    ans += l1 + l2
    heapq.heappush(que,ans)

print(ans)
