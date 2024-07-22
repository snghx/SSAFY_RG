# 수도 요금 경쟁

T = int(input())

for tc in range(1, T+1):
    
    P, Q, R, S, W = map(int, input().split())
    
    # A사 
    a = P * W

    # B사   1) R리터 초과인 경우 2) R리더 이하인 경우
    if W > R : 
        b = Q + S * (W-R)
    else:
        b = Q
        
    if a < b : ans = a
    else : ans = b

    print(f'#{tc} {ans}')





'''
T = int(input())

for test_case in range(1, T+1) :
    P, Q, R, S, W = map(int, input().split())
    a = P*W
    if W <= R:
        b= Q
    else: b= Q + (W-R)*S
    
    if a>b : print(f'#{test_case} {b}') 
    else : print(f'#{test_case} {a}')

'''