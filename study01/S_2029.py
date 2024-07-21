# 몫과 나머지 출력하기

N = int(input())  # tc 개수 입력 받기

for tc in range(1, N+1):
    a, b = map(int, input().split())

    print(f'#{tc} {a//b} {a%b}')
    # print('#{} {} {}'.format(tc, a//b, a%b))
    