T = int(input())
 
for tc in range(1, T+1):
    N,M = map(int,input().split())
    lst = list(map(int, input().split()))
     
 
    for game in range(M):
        i, j = map(int,input().split())
        s = i-1         # 돌 뒤집기 시작 위치
        e = i+j-2       # 돌 뒤집기 종료 위치

        if e > N-1:     # 만약, 종료 위치가 범위 밖이라면 
            e = N-1     # 종료 위치를 범위 안으로 변경

        color = lst[s]  # 돌 색깔 지정 
 
        for change in range(s, e+1):
            lst[change] = color
 
    print(f'#{tc}', *lst)