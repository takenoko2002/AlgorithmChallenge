#グラフの隣接リストによる実装
"""
辺に属性がある場合、構造体やクラスを使う。pythonは辞書でも可。
class edge:
    def __init__(self,to,cost):
        self.to = to
        self.cost = cost

G = []
#edgeクラスを配列に格納する
G.append(edge(1,2))
#配列にアクセス
G[0].to    #1が出力される
G[0].cost  #2が出力される
"""

# V:頂点の集合 E:辺の集合
V,E = map(int,input().split())

#グラフ (iがグラフの頂点、G[i]に隣接するグラフが入っている)
#行数(Vの頂点の数)は決まっているが、カラムに入っている値の数(頂点Vから出る辺の数)は決まっていない
G = [ [] for row in range(V)]

for i in range(E):
    #sからtへの辺を張る
    s,t = map(int,input().split())
    G[s].append(t)    
    #無向グラフの場合は、さらにtからsに辺を張る(お互いに張り合う)
    #G[t].append(s)
    
print(G)

"""
#重み付きグラフの格納
for i in range(E):
    #sからtへコストがcの辺を張る
    s,t,c = map(int,input().split())
    G[s].append(edge(t,c))
    #無向グラフ
    #G[t].append(edge(s,c))

#重み付き無向グラフの出力
for i in range(len(G)):
    for j in range(len(G[i])):
            print(i,G[i][j].to,G[i][j].cost)
"""
