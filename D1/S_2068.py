# 2068번 최대수 구하기

T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    result = max(lst)
    print(f'#{test_case} {result}')