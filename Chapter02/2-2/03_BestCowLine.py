
N = int(input())
S = input()

a = 0
b = N -1 

#
while a <= b:
    #左からみた場合と右から見た場合を比較
    left = False
    for i in range(0,N):
        if a + i > b:
            break
        if S[a + i] < S[b -i]:
            left = True
            break
        elif S[a+i] > S[b -i]:
            left = False
            break

    if left:
        print(S[a],end='')
        a += 1
    else:
        print(S[b],end='')
        b -= 1
print('')

