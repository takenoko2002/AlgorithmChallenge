
#sの文字数
n = int(input())
#tの文字数
m = int(input())

s = input()
t = input()

#DPテーブル
dp = [ [ 0 for col in range(m+1)] for row in range(n+1) ]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] +1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

print(dp[n][m])
