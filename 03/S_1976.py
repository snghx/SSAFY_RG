# 1976. 시각 덧셈 (10m)

T = int(input())

for test_case in range(1, T+1):
    a, b, c, d = map(int, input().split())

    if b + d < 60 :
        H = a + c
        M = b + d
    else :
        H = a + c + 1
        M = (b + d) % 60

    if H > 12 :
        H -= 12
    
    print(f'#{test_case} {H} {M}')