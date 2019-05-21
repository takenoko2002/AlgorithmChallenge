
#品物の数
N = 4
#重さ
w = [2,1,3,2]
#価値
v = [3,2,4,2]
#重さの総和
W = 5

#i番目以降の品物から重さの総和がj以下となるように選ぶ
def rec(i,j):
    res = 0
    if (i == N):
        #もう品物が残っていない
        res = 0
    elif j < w[i] :
        #この品物は入らない(次の品物を試す)
        res = rec(i+1,j)
    else:
        #入れない場合(rec(i+1,j)と入れる場合(rec(i+1,j - w[i])+v[i])両方試す
        # j - w[i] : 入れるので重さを引いて残りの重さを渡す
        # +v[i] : 選んだものの価値
        res = max(rec(i+1,j),rec(i+1,j - w[i])+v[i])
    return res

print(rec(0,W))