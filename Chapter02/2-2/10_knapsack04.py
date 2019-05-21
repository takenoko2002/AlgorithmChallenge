
#品物の数
N = 3
#重さ
w = [3,4,2]
#価値
v = [4,5,3]
#重さの総和
W = 7

#DP化テーブル( N + 1 行 W + 1列) #0で初期化
dp = [ [0 for col in range(W +1)] for row in range(N + 1) ]

#単純に漸化式を実装
#漸化式
#i番目までの品物から重さの総和がj以下となるように選んだときの、価値の総和の最大値
#dp[0][j]=0
#dp[i+1][j] = max( dp[i][j-k*w[i]] +k*v[i] | 0<=k )
#           = max( dp[i][j], dp[i][j-k*w[i]] +k*v[i] | 1<=k)
#           = max( dp[i][j], dp[i][(j-w[i])-k*w[i]] +k*v[i] | 0<=k) +v[i] )
#           = max( dp[i][j], dp[i+1][j-w[i]] +v[i])

#dp[n][j]=0 は初期化時に実現済み
for i in range(N):
    for j in range(W+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j],dp[i+1][j - w[i]] +v[i])       

print(dp[N][W])