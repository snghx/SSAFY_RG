# 큰 놈, 작은 놈, 같은 놈

T = int(input())

for tc in range(1, T+1) :
    a, b = map(int, input().split())

    if a > b : ans = '>'
    elif a < b : ans = '<'
    else : ans = '='

    print(f'#{tc} {ans}')




''' .format()
T = int(input())

for test_case in range(1, T + 1):
    l, r = map(int, input().split())
    
    if l > r : print('#{} {}'.format(test_case, '>'))
    elif l < r : print('#{} {}'.format(test_case, '<'))
    else : print('#{} {}'.format(test_case, '='))
        
'''