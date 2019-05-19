
N = int(input())
R = int(input())
X = list(map(int,input().split()))

X = sorted(X)

i = 0
s = 0

ans = 0

while i < N:
    s = X[i]

    #次の点以降の点がR以内の間は進む
    i += 1
    while (i < N) and (X[i] <= s +R):
        i += 1
    
    #次の点の位置まで進む
    p = X[i-1]
    while(i < N) and (X[i] <= p +R):
        i += 1
    
    ans += 1

print(ans)