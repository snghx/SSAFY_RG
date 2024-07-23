'''2071. 평균값 구하기'''
T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    print(f'#{test_case} {round(sum(arr) / 10)}')   
    
# 받은 10개의 수를 더하고 10으로 나누어 평균 / 반올림