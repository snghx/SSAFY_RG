'''1986. 지그재그 숫자'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 0
    for tc_1 in range(1, N+1):
        if tc_1 % 2 == 0:
            result -= tc_1
        else:
            result += tc_1
    print(f'#{tc} {result}')

