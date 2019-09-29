#ダイクストラ法
#頂点数
V = int(input())
#cost[u][v]は辺e=(u,v)のコスト V*Vの配列
cost = [[ [] for i in range(V)] for j in range(V)]
#頂点sからの最短距離
d = [ [] for i in range(V) ]
#すでに使われたかのフラグ
used = [ [] for i in range(V) ]
#INF(10億)
INF = 1000000000

def dijkstra(s):
    for i in range(V):
        d[i] = INF
    for i in range(V):
        used[i] = False
    #始点の距離は0
    d[s] = 0

    while(True):
        v = -1
        #まだ使われていない頂点のうち距離が最小のものを探す
        for u in range(V):
            if ( not used[u] and ( v == -1 or d[u] < d[v])) :
                v = u
        if v == -1 :
            break
        used[v] = True
        for u in range(V):
            d[u] = min(d[u],d[v]+cost[v][u])
