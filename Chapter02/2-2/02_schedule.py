#終了時刻が早い仕事を選択し続ける

#２次元配列のソートに使う
from operator import itemgetter

#入力
work_amount = int(input())
start_time = list(map(int,input().split()))
end_time = list(map(int,input().split()))

#各仕事の開始時刻と終了時刻をペアにした配列
work_time = list(map(list,zip(start_time,end_time)))

#work_timeを終了時刻でソート
sorted_work_time=sorted(work_time, key=itemgetter(1))

#こなした仕事の量
worked_amount = 0
#こなした後の時間
now_time = 0

for i in range(work_amount):
    #今の時刻とスタート時刻を比較し、まだスタート時刻になっていない場合
    if now_time < sorted_work_time[i][0] :
        #仕事の回数を増やして今の時刻を終了時刻にする
        worked_amount += 1
        now_time = sorted_work_time[i][1]

print(worked_amount)

