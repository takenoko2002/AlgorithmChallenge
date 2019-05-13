#4回くじびきする

#紙の枚数
n = int(input())

#数字の和
m = int(input())

#くじの中の紙のリスト
li = list(map(int,input().split()))
f = False

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if (li[i] + li[j] + li[k] + li[l] == m):
                    f = True

if (f):
    print('yes')
else:
    print('No')
