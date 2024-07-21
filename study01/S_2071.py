# 평균값 구하기

T = int(input())

for tc in range(1, T+1):
    list_a = list(map(int, input().split()))

    ans = sum(list_a)/len(list_a)
    
    print('#{tc} {ans}')

