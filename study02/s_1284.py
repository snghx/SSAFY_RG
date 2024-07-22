# 1284. 수도 요금 경쟁
# 9:08 시작 9:12 종료

T = int(input())

for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    '''
    A사, 1리터당 P원 
    B사, R리터 이하인 경우, Q / R리터 이상인 경우, Q + 1리터당 S원
    '''
    
    price_a = W * P
    price_b = 0
    
    if W <= R:
        price_b = Q
    else:
        price_b = Q + S*(W-R)
    
    print(f"#{t} {min(price_a, price_b)}")