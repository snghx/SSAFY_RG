# 수도 요금 경쟁

T = int(input())

P, Q, R, S, W = map(int, input().split())

for tc in range(1, T+1):
    
    # A사 
    a = P * W

    # B사   1) R리터 초과인 경우 2) R리더 이하인 경우
    if W > R : 
        b = R * Q + S * (W-Q)
    else:
        b = W * Q
        
    if a < b : ans = a
    else : ans = b

    print(f'#{tc} {ans}')