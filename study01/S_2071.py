# 평균값 구하기

T = int(input())

for tc in range(1, T+1):
    list_a = list(map(int, input().split()))

    ans = round(sum(list_a)/len(list_a))
    
    print(f'#{tc} {ans}')


'''
T = int(input())
for test_case in range(1, T+1) :
    list_n = list(map(int, input().split()))
    
    s = 0
    for i in range(10):
        s += list_n[i]
        
    m  = round(s / 10)
    
    print('#' + str(test_case) + ' ' + str(m))
'''