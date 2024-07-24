'''1284. 수도 요금 경쟁'''
T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    
    # A회사 이용 시
    A_com = W * P
    # B회사 이용 시
    if W > R:
        B_com = Q + (W - R) * S
    else:
        B_com = Q

    if A_com > B_com:
        result = B_com
    elif A_com < B_com:
        result = A_com
    
    print('#{} {}'.format(tc, result))
