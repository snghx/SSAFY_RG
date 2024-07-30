

T = int(input())

mth_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for tc in range (1, T+1): # 주어진 TC만큼 돌아간다.
    lst = list(map(int,input().split()))
    m1 = lst[0]
    m2 = lst[2]
    d1 = lst[1]
    d2 = lst[3]

    day = 0
    if m1 == m2:
        day = d2 - d1 + 1
    else:
        day = mth_day[m1] - d1 +1 + d2 #첫달 막달
        for i in range(m1+1, m2): # 1월과 5월이면, 4, 0 1 2 3 4 
           
            day +=mth_day[i]
    print(f'#{tc} {day}')

