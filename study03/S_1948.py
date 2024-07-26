# 날짜 계산기

day = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 
       7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

T = int(input())

for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    d_sum = day[m1] - d1 + 1

    if m2 - m1 > 1:
        for m in range(m1+1, m2):
            d_sum += day[m]
        d_sum += d2

    print(f'#{tc} {d_sum}')