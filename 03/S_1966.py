# 1966. 숫자를 정렬하자 (9m)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    number.sort()
    print(f'#{test_case}',*number)
