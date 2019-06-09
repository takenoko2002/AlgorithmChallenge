
#入力は省く

MAX_N = 100
MAX_K = 7

#入力：Tは情報のタイプ
T = [0] * MAX_K
X = [0] * MAX_K
Y = [0] * MAX_K

n = 100
k = 7

#UnionFind木の実装
par = [0] * MAX_N  #親
rank = [0] * MAX_N #木の深さ

#n要素で初期化
def init(n):
    for i in range(n):
        par[i] = i
        rank[i] = 0

#木の根を求める
def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

#xとyの属する集合を併合
def unite(x,y):
    x = find(x)
    y = find(y)
    #もとから同じ集合のときは何もしない
    if (x == y):
        return
    #rankが小さいものから大きいもの辺を張る
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        #ランクが同じときはxに辺を貼ってxのランクを増やす
        if rank[x] == rank[y]:
            rank[x] += 1

#xとyが同じ集合に属するかどうか
def same(x,y):
    return find(x) == find(y)

#以下 POJ 1182
#UnionFind木を初期化
# x, x + N, x +  2*N を x-A、x-B、x-C の要素とする
init(n*3)

ans = 0
for i in range(k):
    t = T[i]
    #X,Yは 0 から N-1の範囲にする
    x = X[i] -1
    y = Y[i] -1

    #正しくない番号
    if x<0 or n<=x or y<0 or n<=y :
        ans +=1
        continue

    if t == 1 :
        #xとyは同じ種類という情報
        if same(x,y+n) or same(x,y+2*n):
            ans+=1
        else:
            unite(x,y)
            unite(x+n,y+n)
            unite(x+n*2,y+n*2)
    else:
        #xはyを食べるという情報
        if same(x,y) or same(x,y+2+n):
            ans+=1
        else:
            unite(x,y+n)
            unite(x+n,y+2*n)
            unite(x+n*2,y)

print(ans)
