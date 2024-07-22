'''2068. 최대수 구하기'''
T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    print(f'#{test_case} {max(num)}') # 받은 수(num) 중에 max 값