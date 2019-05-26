
#最長増加部分列問題
n =int(input())

a = list(map(int,input().split()))

dp = [ 0 ] * n

res = 0
for i in range(n):
    dp[i]=1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i],dp[j]+1)
    res = max(res,dp[i])

print(res)
