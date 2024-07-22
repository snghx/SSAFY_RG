# 1986 지그재그 숫자

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ans = 0 

    # 1부터 시작, N의 수까지
    for i in range(1, N+1):

        # 홀수는 더하기
        if i % 2 == 1 : ans += i

        # 짝수는 빼기
        else : ans -= i

    print(f'#{tc} {ans}')

