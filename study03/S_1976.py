# 시각 덧셈


T = int(input())

for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    h = h1 + h2
    m = m1 + m2
    
    if m >= 60:
        m %= 60
        h +=1
        
    if h >= 13:
        h %=12

        if h == 0:   # 24인 경우 -> 0 이라고 나오기 때문에
            h = 12

    print(f'#{tc} {h} {m}')