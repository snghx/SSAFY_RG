'''1948. 날짜 계산기 / 35분'''
T = int(input())

cal = {1 : 31, 2: 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
# 달을 dict로 받음

for tc in range(1, T+1):
    M1, D1, M2, D2 = map(int, input().split())  # 월, 일을 map으로 받음
    ans = 0

    if M1 == M2:    # 같은 달일 때
        ans = D2 - D1 + 1
    else:           # 다른 달일 때
        ans = cal[M1] - D1 + 1
        # 시작하는 달 : '총 일 - 현재 + 1'

        for months in range(M1+1, M2):
            ans += cal[months]
        # 중간의 달 : 시작 달 + 1 ~ 마지막 달 - 1까지 총 일 수
        ans += D2
        # 마지막 달 : 입력된 일 수
    print('#{} {}'.format(tc, ans))