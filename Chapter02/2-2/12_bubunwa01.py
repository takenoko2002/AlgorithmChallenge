
n = int(input())
a = list(map(int,input().split()))
m = list(map(int,input().split()))
K = int(input())

dp = [-1] * (K+1)

dp[0] = 0

#i番目まででKを作る際に余る最大のi番目の個数(作れない場合は-1)
for i in range(n):
    for j in range(K+1):
        #i番目までで余る
        if dp[j] >= 0 :
            dp[j] = m[i]
        #a[i]を使うとjを超える または i番目までに j-a[i] を作れないなら i番目までに jは作れない
        elif j < a[i] or dp[j-a[i]] <= 0 :
            dp[j] = -1
        #i番目までに j-a[i] を作れるなら あまりをもう一つ使えば(-1すれば) jを作れる
        else :
            dp[j] = dp[j - a[i]] -1

if dp[K] >= 0:
    print('Yes')
else:
    print('No')
