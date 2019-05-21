
#品物の数
N = 4
#重さ
w = [2,1,3,2]
#価値
v = [3,2,4,2]
#重さの総和
W = 5

#DP化テーブル( N + 1 行 W + 1列) #0で初期化
dp = [ [0 for col in range(W +1)] for row in range(N + 1) ]

#単純に漸化式を実装
#漸化式
#dp[n][j]=0
#dp[i][j] ---- dp[i+1][j] (j < w[i])
#          |-- max ( dp[i+1][j] , dp[i+1][j - w[i] + v[i] ] )

#dp[n][j]=0 は初期化時に実現済み
for i in range(N-1,-1,-1):
    for j in range(0,W+1):
        if j < w[i]:
            dp[i][j] = dp[i+1][j]
        else:
            dp[i][j] = max(dp[i+1][j],dp[i+1][j - w[i]] +v[i])       

print(dp[0][W])