# 새로운 불면증 치료법



T = int(input())


for tc in range(1, T+1):
    N = int(input())
    cnt = 1                     # 처음부터 1번은 세니까, 초기값 1
    set = set()                    # 0~9까지 담을 set 만들기


    while len(set) < 10 :       # len(set) == 10이 되면, 멈추기 
        for s in str(N):
            set.add(s)
            N *= cnt
            cnt += 1
    print(f'#{tc} {cnt}')
            