# 1284. 수도 요금 경쟁 (9m)

T = int(input())

for test_case in range(1,T+1):
    P,Q,R,S,W = map(int, input().split())

    # A사를 선택했을 때 요금
    A = P * W 

    # B사를 선택했을 때 요금
    if W < R :
        B = Q
    elif W > R:
        B = Q + (W - R)*S

    if A < B :
        result = A
    elif A > B:
        result = B

    print(f'#{test_case} {result}')
