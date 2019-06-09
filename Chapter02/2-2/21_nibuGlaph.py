#無向グラフの2色の色分け
#入力 V:頂点の数 G:グラフ color:グラフiの色(1 or -1)
"""
入力例1
VとE
3 3
辺の情報
0 1
0 2
1 2

入力例2
VとE
4 4
辺の情報
0 1
0 3
1 2
2 3
"""

#グラフ (iがグラフの頂点、G[i]に隣接するグラフが入っている)
#行数(Vの頂点の数)と辺の数Eは決まっているが、カラムに入っている値の数(頂点Vから出る辺の数)は決まっていない
V,E = map(int,input().split())
G = [ [] for row in range(V)]

for i in range(E):
    #sからtへの辺を張る
    s,t = map(int,input().split())
    G[s].append(t)
    #無向グラフ
    G[t].append(s)

color = [0] * V

#頂点を 1 と -1で塗っていく
def dfs(v,c):
    #頂点vをcで塗る
    color[v] = c
    for i in range(len(G[v])):
        #隣接している頂点が同じ色ならfalse
        if color[G[v][i]] == c :
            return False
        #隣接している頂点がまだ塗られてないなら -c で塗る
        if color[G[v][i]] == 0 and  (not dfs(G[v][i],-c)) :
            return False
    #すべての頂点を塗れたらTrue
    return True 

for i in range(V):
    if color[i] == 0 :
        #まだ頂点iが塗られていなければ1で塗る
        if not(dfs(i,1)) :
            print('No')
            exit()

print('Yes')