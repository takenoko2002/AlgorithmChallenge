
#各コインの枚数
maisu = list(map(int,input().split()))
A = int(input())

li_kouka =[1,5,10,50,100,500]

ans = 0

#大きいものから使う
for i in range(len(li_kouka)-1,-1,-1):
    #コインを使う枚数
    t = min((A//li_kouka[i]),maisu[i])
    A -= t * li_kouka[i]
    ans += t

print(ans)
