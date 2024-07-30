'''1976. 시각 덧셈 / 60분'''
T = int(input())

for tc in range(1, T+1):
    H1, M1, H2, M2 = list(map(int, input().split()))
    # 시간과 분을 받음
    H3 = H1 + H2 
    M3 = M1 + M2
    # 이후 출력할 시간과 분을 정의

    if M1 + M2 >= 60:   # 분의 합이 60을 넘을 때
        M3 -= 60
        H3 += 1
    
    if H1 + H2 > 12:    # 시간의 합이 12를 넘을 때
        H3 -= 12

    print('#{} {} {}'.format(tc, H3, M3))