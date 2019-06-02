
#優先度キューを用いて最大値を取り出しながら進んでいく
import heapq

# N:スタンドの数、L:ゴールまでの距離、P:はじめに積まれているガソリンの量
N,L,P = map(int,input().split())

A = [10,14,20,21]
B = [10,5,2,4]

#簡単のためゴールをガソリンスタンドに追加
A.append(L)
B.append(0)

#順位キュー
que = []

# ans:補給回数 pos:今いる場所 tank:タンクのガソリンの量
ans = 0
pos = 0
tank = P 

for i in range(N+1):
    #次に進む距離
    d = A[i] - pos

    #十分な量になるまでガソリンを補給(次のスタンドまでたどりつけない)
    while( (tank - d) < 0 ):
        #スタンドが足りない場合
        if len(que) == 0:
            print(-1)
            exit()
        #ガソリンスタンドから給油する
        tank += heapq.heappop(que) * -1
        ans += 1
    
    #次のスタンドまでたどりつける
    tank -= d
    pos = A[i]
    heapq.heappush(que,B[i] * -1)
    
print(ans)