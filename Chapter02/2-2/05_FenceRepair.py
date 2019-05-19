
N = int(input())
L = list(map(int,input().split()))

ans = 0

#板が1本になるまで
while N > 1:
    #一番短い板、次に短い板を求める
    mii1 = 0
    mii2 = 1 
    #先頭から2つを比較して小さいほうの添字をmii1、大きい方の添字をmii2にする
    if L[mii1] > L[mii2]:
        mii1,mii2= mii2,mii1
    
    #３番目(添字2)以降を確認していき、mii1を一番短い板の添字、mii2を次に短い板の添字にする
    for i in range(2,N):
        if L[i] < L[mii1]:
            mii2 = mii1
            mii1 = i
        elif L[i] < L[mii2]:
            mii2 = i
    #mii1,mii2を併合する
    t = L[mii1] + L[mii2]
    ans += t
    #末尾は以降使わないため、mii1が末尾なら入れ替え
    if mii1 == N -1:
        mii1,mii2 = mii2,mii1
    
    #併合した値をmii1(今まで一番小さい値があった場所に)
    L[mii1] = t
    #mii2はいらないので末尾へ
    L[mii2] = L[N -1]
    #配列を一個狭める(末尾を範囲外へ)
    N -= 1

print(ans)