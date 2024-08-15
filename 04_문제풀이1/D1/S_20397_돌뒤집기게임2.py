T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    lst = list(map(int, input().split()))

    i,j = map(int, input().split())

    start = i-1        # 시작위치 지정

    for s in range(j):
        if (start-s< 0) or (start+s >N-1):     # 주어진 돌을 벗어나는 경우 뒤집기 중지
            break
        if (lst[start-s] == lst[start+s]):     # 시작위치를 기준으로 마주보는 돌이 같은 색일 경우
            lst[start-s] = 1 - lst[start-s]    # 돌 뒤집기
            lst[start+s] = 1 - lst[start+s]

    print(f'#{tc}', *lst)
    