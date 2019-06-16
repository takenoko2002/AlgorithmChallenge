#重み付きグラフの辺の情報のみによる実装
class edge:
    def __init__(self,source,to,cost):
        #pythonはfromが予約語なのでsourceを使用
        self.source = source
        self.to = to
        self.cost = cost

# V:頂点の集合(数) E:辺の集合(数)
V,E = map(int,input().split())

#各頂点への最短距離(DPテーブル)
d = [0] * V

#各辺の情報をesに格納(重み付き辺)
es = [] 
for i in range(E):
    source,to,cost = map(int,input().split())
    es.append(edge(source,to,cost))
    #無向グラフ
    es.append(edge(to,source,cost))

#INF(10億)
INF = 1000000000

#s番目の頂点から各頂点への最短距離を求める
#閉路があった場合用に更新がなければループを抜ける
def short_path(s):
    for i in range(V):
        d[i] = INF
    d[s] = 0
    while(True):
        update = False
        for i in range(len(es)):
            e = es[i]
            """
            始点Sから頂点iまでの距離は、
            すべての辺について、
                その時点のSからfrom(source)までの距離にcostを足したもの と、
                その時点のSからtoまでの距離  を
                比べて小さい方を繰り返し選択することによって求められる
            """
            if d[e.source] != INF and d[e.to] > d[e.source] + e.cost :
                d[e.to] = d[e.source] + e.cost
                update = True
        if not(update) :
            break

short_path(4)

print(d)

"""
入力用(P.94　下の図)
7 10
0 1 2
0 2 5
1 2 4
1 3 6
1 4 10
2 3 2
3 5 1
4 5 3
4 6 5
5 6 9
"""