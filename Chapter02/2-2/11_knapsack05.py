
#wiの範囲が10^7になってめっちゃ重くなったナップサック問題

#品物の数
N = 4
#重さ
w = [2,1,3,2]
#価値
v = [3,2,4,2]
#重さの総和
W = 5

#DPテーブル( N + 1 行 W + 1列) #INFで初期化
dp = [ [1000000000 for col in range(N * max(v) +1)] for row in range(N + 1) ]

#価値に対する最小の重さ
#dp[i+1][j] i番目までの品物から価値の総和がjとなるように選んだときの重さの総和の最小値
# (そのような解が存在しない場合は十分大きなINF)
#初期値
#dp[0][0]=0
#dp[0][j] = INF
#i番目までの品物から価値の総和がjとなるように選ぶためには
# i-1 番目までの品物からかちの総和がjとなるように選ぶ 
# i-1 番目までの品物から価値の総和が j -v[i]となるように選ぶ、i番目の品物を加える
#漸化式
#dp[i+j][j]=min(dp[i][j],dp[i][j-v[i]]+w[i])

#dp[n][j]=0 は初期化時に実現済み
dp[0][0] = 0
for i in range(N):
    for j in range((max(v) * N) +1):
        #
        if j < v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j],dp[i][j - v[i]] +w[i])

res = 0
for i in range((max(v) * N) +1):
    if dp[N][i] <=W:
        res = i
print(res)
