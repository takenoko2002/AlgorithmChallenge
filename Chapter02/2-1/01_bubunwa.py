#部分和問題

#整数の数
n = int(input())
#整数のリスト
li = list(map(int,input().split()))
#答え
k = int(input())

#iまででsumを作って、残りi以降を調べる
def DepthFirstSearch(i,sum):
    #n個決め終わったら sum が k と等しいか返す
    if i == n :
        return sum == k
    #li[i]を使わない場合
    if (DepthFirstSearch(i+1,sum)):
        return True
    #li[i]を使う場合
    if (DepthFirstSearch(i+1,sum+li[i])):
        return True
    
    #li[i]を使う使わないにかかわらずkが作れないのでfalseを返す
    return False

if DepthFirstSearch(0,0):
    print('yes')
else:
    print('No')
